https://lms.clarusway.com/mod/lesson/view.php?id=10269&pageid=8667
#! Serializers
# In web development, many applications rely on REST APIs to allow the front end to talk to the back end. If you’re deploying a React application you’ll need an API to allow React to consume information from the database.

# Data from the database is transferred to the frontend in the form of JSON, XML, or other content types. But as you know, the data in our databases is not in this format. Serializers allow complex data in databases to be converted to native Python datatypes that can then be easily rendered into JSON, XML, or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.

# The serializers in the REST framework work very similarly to Django's Form and ModelForm classes. We provide a Serializer class and create fields according to our model. Lets remember our model:

from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField()

# Then let's create a serializers.py file in our fscohort_api folder. We'll declare a serializer that we can use to serialize and deserialize data that corresponds to Student objects. Declaring a serializer looks very similar to declaring a form:

from rest_framework import serializers

class StudentDefaultSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    number = serializers.IntegerField()

# NOT: It will be useful to serialize the automatically generated ids in the model and send them to the frontend.

# Serializing Objects
# We can now use StudentDefaultSerializer to serialize a Student, or list of Students. Again, using the Serializer class looks a lot like using a Form class.

serializer = StudentDefaultSerializer(student)
serializer.data
#* {'id': '1', 'first_name': 'Edward', 'last_name': 'Benedict', 'number':'123'}

# At this point, we've translated the model instance into Python native datatypes. To finalize the serialization process we render the data into JSON.
from rest_framework.renderers import JSONRenderer

json = JSONRenderer().render(serializer.data)
json
#* b'{"id":"1","first_name":"Edward","last_name":"Benedict","number":"123"}'

# Deserializing Objects
# Deserialization is similar. First, we parse a stream into Python native datatypes...
import io
from rest_framework.parsers import JSONParser

stream = io.BytesIO(json)
data = JSONParser().parse(stream)

# ...then we restore those native datatypes into a dictionary of validated data.
serializer = StudentDefaultSerializer(data=data)
serializer.is_valid()
#* True
serializer.validated_data
#* {'id': '2', 'first_name': 'Walter', 'last_name': 'White', 'number':'321'}

# Saving instances
# If we want to be able to return complete object instances based on the validated data we need to implement one or both of the .create() and .update() methods.

# If your object instances correspond to Django models you'll also want to ensure that these methods save the object to the database. For example, if Student was a Django model (In our project it is a model) , the methods might look like this:
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.number = validated_data.get('number', instance.number)
        instance.save()
        return instance

# Now when deserializing data, we can call .save() to return an object instance, based on the validated data.
student = serializer.save()

# Calling .save() will either create a new instance, or update an existing instance, depending on if an existing instance was passed when instantiating the serializer class:

#* .save() will create a new instance.
serializer = StudentDefaultSerializer(data=data)

#* .save() will update the existing `student` instance.
serializer = StudentDefaultSerializer(student, data=data)

# Both the .create() and .update() methods are optional. You can implement either neither, one, or both of them, depending on the use-case for your serializer class.

# Validation
# When deserializing data, you always need to call is_valid() before attempting to access the validated data or save an object instance. If any validation errors occur, the .errors property will contain a dictionary representing the resulting error messages. For example:
serializer = StudentDefaultSerializer(data={'first_name': 'victor', 'last_name': 'Hugo'})
serializer.is_valid()
#* False
serializer.errors
#* {'first_name': ['Enter a valid first_name.'], 'number': ['This field is required.']}

#! ModelSerializer
# We said on the previous page that serializers are very similar to Form structures in Django. It is possible to make a serializer class using the Student model we have, as in the forms. We can do this by declaring serializers that work very similar to Django’s Model forms. The ModelSerializer class provides a shortcut that lets you automatically create a Serializer class with fields that correspond to the Model fields.

# The ModelSerializer class is the same as a regular Serializer class, except that:
    # It will automatically generate a set of fields for you, based on the model.
    # It will automatically generate **validators **for the serializer, such as unique_together validators.
    # It includes simple default implementations of .create() and .update() .

# Declaring a ModelSerializer looks like this:
from rest_framework import serializers
from fscohort.models import Student

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'number']  

# By default, all the model fields on the class will be mapped to a corresponding serializer field.
    # We imported the serializer class from the rest_framework module.
    # Then we imported the model we wanted serializer for.
    # Then like the model forms class, we created a serializer class. This is called the model serializer class.
    
#! Other Serizalizer Types
# NOT : Other serializer Types are advenced topics and you can check documentation for detailed information.

#? HyperlinkedModelSerializer
# The HyperlinkedModelSerializer class is similar to the ModelSerializer class except that it uses hyperlinks to represent relationships, rather than primary keys.

# By default the serializer will include a url field instead of a primary key field.

# The url field will be represented using a HyperlinkedIdentityField serializer field, and any relationships on the model will be represented using a HyperlinkedRelatedField serializer field.

# You can explicitly include the primary key by adding it to the fields option, for example:
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['url', 'id', 'first_name', 'last_name', 'number']

# When instantiating a HyperlinkedModelSerializer you must include the current request in the serializer context, for example:
serializer = StudentSerializer(queryset, context={'request': request})

# Doing so will ensure that the hyperlinks can include an appropriate hostname, so that the resulting representation uses fully qualified URLs, such as:
http://api.example.com/students/1/

# Rather than relative URLs, such as:
/students/1/


#? ListSerializer
# The ListSerializer class provides the behavior for serializing and validating multiple objects at once. You won't typically need to use ListSerializer directly, but should instead simply pass many=True when instantiating a serializer.

# When a serializer is instantiated and many=True is passed, a ListSerializer instance will be created. The serializer class then becomes a child of the parent ListSerializer

# The following argument can also be passed to a ListSerializer field or a serializer that is passed many=True:

# allow_empty This is True by default, but can be set to False if you want to disallow empty lists as valid input.

#? BaseSerializer
# BaseSerializer class that can be used to easily support alternative serialization and deserialization styles. This class implements the same basic API as the Serializer class There are four methods that can be overridden, depending on what functionality you want the serializer class to support:

# .to_representation() - Override this to support serialization, for read operations.
# .to_internal_value() - Override this to support deserialization, for write operations.
# .create() and .update() - Override either or both of these to support saving instances.
# Because this class provides the same interface as the Serializer class, you can use it with the existing generic class-based views exactly as you would for a regular Serializer or ModelSerializer.
# The only difference you'll notice when doing so is the BaseSerializer classes will not generate HTML forms in the browsable API. This is because the data they return does not include all the field information that would allow each field to be rendered into a suitable HTML input.


#? Third party packages
# The third party packages are also available.

#? Serializer Fields
# Like Model fields and Form fields in Django, serializers have fields. Serializer fields handle converting between primitive values and internal datatypes. They also deal with validating input values, as well as retrieving and setting the values from their parent objects.
# Note :The serializer fields are declared in fields.py, but by convention you should import them using from rest_framework import serializers and refer to fields as serializers.FieldName. For example:
class StudentDefaultSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()  

# Core Arguments
# read_only , write_only, required, default, allow_null, source, validators, error_messages, label, help_text, initial, style for example:
#* Use  for the input.
password = serializers.CharField(
    style={'input_type': 'password'}
)

# FIELDS
# Serializer fields similar to model and form fields has:

# BooleanField
# CharField
# SlugField
# IntegerFıeld
# DateTimeField
# ...