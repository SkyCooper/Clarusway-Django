https://lms.clarusway.com/mod/lesson/view.php?id=6897&pageid=8584
#! Relationships in Django models
# Django models work with relational database systems (RDBMS) by default to accommodate relationships between them. Database relationships, in their most basic form, are used to connect records based on a key or id, resulting in better data management, query accuracy, and less duplicate data, among other benefits.

# Relational database systems support three relationships: one to many, many to many, and one to one. Django models support the same three relationships.


# Now, let's create a new app named dj_relationships and learn more about each relationship in detail.
#! (Don't forget to add your app to INSTALLED_APPS)
                                                                                                      
#? One-To-One Relationship
# One-to-one relationships occur when there is exactly one record in the first table that corresponds to one record in the related table. Here we have an example where we know that each language has one creator.

# Now, let's create our models;
# dj_relationshipst/models.py
class Creator(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Languages(models.Model):
    creator = models.OneToOneField(Creator, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#! We define the relationship with models.OneToOneField

# on_delete (used in one-to-one and one-to-many) argument lets you specify what happens to the other party when one party is removed. In our model with models.CASCADE if Creator instance is deleted, Language records referencing the Creator instance is also deleted. You can find other options here.

# and run python manage.py makemigrations and python manage.py migrate commands.

# Making Queries
# Open your django interactive console ;

>>> from dj_relationships.models import Creator, Languages
>>> p = Creator.objects.create(first_name="Guido van", last_name="Rossum")
>>> j = Creator.objects.create(first_name="James", last_name="Gosling")
>>> js = Creator.objects.create(first_name="Brenden", last_name="Eich")
>>> pyt = Languages.objects.create(creator=p, name="python")
>>> java = Languages.objects.create(creator=j, name="java")
>>> javascript = Languages.objects.create(creator=js, name="java script")
>>> p
<Creator: Guido van Rossum>
>>> j
<Creator: James Gosling>
>>> js
<Creator: Brenden Eich>
>>> python
<Languages: python>
>>> java
<Languages: java>
>>> javascript
<Languages: java script>

#* Now, let's make some query;

# Access the Languages object and its fields through Creator object 
# (use lowercase model name Languages --> languages)
>>> p.languages.name
'python'

# Access the Creator object and its fields through the Languages object
>>> pyt.creator.first_name
'Guido van'

# Get Creator objects through Languages with name startswith "J"
>>> Creator.objects.filter(languages__name__startswith="J")
<QuerySet [<Creator: James Gosling>, <Creator: Brenden Eich>]>

# Get Languages objects through Creator with first_name startswith "J"
>>> Languages.objects.filter(creator__first_name__startswith="j")
<QuerySet [<Languages: java>]>

#? One-To-Many Relationship
# One-To-Many relationship occurs when a parent record in one table can potentially reference several child records in another table. In a one-to-many relationship, the parent is not required to have child records.

# Let's add a Framework model to our dj_relationships/models.py file.
class Creator(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Languages(models.Model):
    creator = models.OneToOneField(Creator, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Frameworks(models.Model):
    languages = models.ForeignKey(Languages, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# We define the relationship with models.ForeignKey
# and run python manage.py makemigrations and python manage.py migrate commands.

# Making Queries
# Open your django interactive console ;

>>> from dj_relationships.models import Creator, Languages, Frameworks
# get Languages objects from db
>>> pyt = Languages.objects.get(name="python")
>>> java = Languages.objects.get(name="java")
>>> javascript=Languages.objects.get(name="java script")

# create Frameworks objects
>>> django=Frameworks.objects.create(languages=pyt, name="django")   
>>> flask=Frameworks.objects.create(languages=pyt, name="flask")  
>>> spring=Frameworks.objects.create(languages=java, name="spring")
>>> struts=Frameworks.objects.create(languages=java, name="struts") 

>>> django
<Frameworks: django>
>>> flask
<Frameworks: flask>
>>> spring
<Frameworks: spring>
>>> struts
<Frameworks: struts>

#* Now, let's make some query;

# Access the Languages object and its fields through Frameworks object
>>> django.languages.name
'python'
>>> django.languages.creator   
<Creator: Guido van Rossum>

# Access the Frameworks objects through Languages object
# (use lowercase model name and underscore set Frameworks--> frameworks_set)
>>> pyt.frameworks_set.all() 
<QuerySet [<Frameworks: django>, <Frameworks: flask>]>
>>> pyt.frameworks_set.filter(name__startswith="f")
<QuerySet [<Frameworks: flask>]>

# Get Frameworks objects through Languages with name "java"
>>> Frameworks.objects.filter(languages__name="java") 
<QuerySet [<Frameworks: spring>, <Frameworks: struts>]>

# Get Languages objects through Frameworks with name "flask"
>>> Languages.objects.filter(frameworks__name="flask")     
<QuerySet [<Languages: python>]>

#? Many-To-Many Relationship
# Many-To-Many relationship occurs when a parent record in one table contains several child rows in another table and vice versa.

# Let's add a Programmer model to our dj_relationships/models.py file.
class Creator(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Languages(models.Model):
    creator = models.OneToOneField(Creator, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Frameworks(models.Model):
    languages = models.ForeignKey(
        Languages, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Programmer(models.Model):
    framework = models.ManyToManyField(Frameworks, db_table="dd")
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

# We define the relationship with models.ManyToManyField

# and run python manage.py makemigrations and python manage.py migrate commands.

# Making Queries
# Open your django interactive console ;

>>> from dj_relationships.models import Frameworks, Programmer
# get Frameworks objects from db
>>> django=Frameworks.objects.get(name="django") 
>>> flask=Frameworks.objects.get(name="flask")   
>>> struts=Frameworks.objects.get(name="struts")         
>>> spring=Frameworks.objects.get(name="spring") 

# create Programmer objects
>>> henry=Programmer.objects.create(first_name="henry", last_name="forester") 
>>> aaron=Programmer.objects.create(first_name="aaron", last_name="a")

# create relationships between Frameworks objects and Programmer objects
>>> henry.framework.add(struts, django) 
>>> aaron.framework.add(django,flask)

#* Now, let's make some query;
# Access the Frameworks objects through Programmer object
>>> henry.framework.all() 
<QuerySet [<Frameworks: django>, <Frameworks: struts>]>
>>> henry.framework.filter(name__startswith="d")
<QuerySet [<Frameworks: django>]>

# Access the Programmer objects through Frameworks object
# (use lowercase model name and underscore set Programmer --> programmer_set)
>>> django.programmer_set.all()
<QuerySet [<Programmer: henry forester>, <Programmer: aaron a>]>
>>> django.programmer_set.filter(first_name__startswith="a") 
<QuerySet [<Programmer: aaron a>]>

# Get Frameworks objects through Programmer with name "henry"
>>> Frameworks.objects.filter(programmer__first_name="henry") 
<QuerySet [<Frameworks: django>, <Frameworks: struts>]>

# Get Programmer objects through Frameworks with name startswith "d"
>>> Programmer.objects.filter(framework__name__startswith="d")  
<QuerySet [<Programmer: aaron a>, <Programmer: henry forester>]>