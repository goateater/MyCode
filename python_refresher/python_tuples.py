#!/usr/bin/env python

# An empty tuple in Python would be defined as:
#tuple = ()

# A comma is required for a tuple with one item
#tuple = (3, )


personInfo = ("Diana", 32, "New York")
name,age,country,career = ('Diana',32,'Canada','CompSci')

print ("Your name is", personInfo[0], "Your age is", personInfo[1], "and you reside in the city of ", personInfo[2])


print(personInfo[0])
print(personInfo[1])
print(country)

print("If you have an existing tuple, you can append to it with the + operator.  You can only append a tuple to an existing tuple.")
x = (3,4,5,6)
x = x + (1,2,3)
print(x)

print("Converting Tuples")
print("Tuple to list to convert a list to a tuple you can use the tuple() function.")
listNumbers = [6,3,7,4]
x = tuple(listNumbers)
print(listNumbers),(type(listNumbers))
print(x), (type(x))

print("\n")
print("You can convert an existing tuple to a list using the list() function:")
x = (4,5)
listNumbers = (list(x))
print(listNumbers), (type(listNumbers))

print("\n")
print("Tuple to string If your tuple contains only strings (text) you can use:")
person = ('Diana', 'Canada', 'CompSci')
print(person)
s = ' '.join(person)
print(s)

print("\n")

print("Sort a tuple")
print("Tuples are arrays you cannot modify and dont have any sort function. You can however use the sorterd() function /"
      "which returns a list. This list can be converted to a new tuple. Keep in mind a tuple cannot be modified, we /"
      "simply create a new tuple that happens to be sorted.")
person = ('Alison','Victoria','Brenda','Rachel','Trevor')
print("Not Sorted: "),(person), (type(person))
person = tuple(sorted(person))
print("Sorted: "),(person), (type(person))