color = 'red'  # str type variable
season = 'summer'
price = 250  # int type variable
print(color, price, season)

a = 5
b = 55
c = 555
c = a
b = c
a = b

print(a, b, c, sep=', ')

fruit1 = 'Apple'
fruit2 = 'Orange'
print(2*fruit1 + " " + 3*fruit2)

xx= 555
phrase = 'I have %d %s and %.2f brothers' % (a, 438, b)  
print ("phrase: ", phrase)

sentence = "apologizing is a virtue"

print("%.11s" % phrase)  # we get first 11 characters of the string

print('%(amount)d pounds of %(fruit)s left' % {'amount': 33, 'fruit':'bananas'})

fruit = 'Orange'
vegetable = 'Tomato'
amount = 4
print('The amount of {} we bought is {} pounds'.format(fruit, vegetable, amount ))

print('{0} is the most {adjective} state of the {country}'.format('California', country='USA', adjective='crowded'))