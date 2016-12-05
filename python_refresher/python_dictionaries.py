#!/usr/bin/env python

print("Python dictionaries")
print("===================")
print("A dictionary can be thought of an an unordered set of key:value pairs.")
print("A pair of braces creates an empty dictionary: {}.")
print("Each element can map to a certain value. An integer or string can be used for the index.")
print("Dictionaries do not have an order. Let us make a simple dictionary.")

print("\n")

words= {}
words["Hello"] = "Bonjour"
words["Yes"] = "Oui"
words["No"] = "Non"
words["Bye"] = "Au Revoir"

print(words["Hello"])
print(words["No"])
print("\n")

dict = {}
dict['Ford'] = "Car"
dict['Python'] = "The Python Programming Language"
dict[2] = "This sentence is stored here."

print dict['Ford']
print dict['Python']
print dict[2]


print("Manipulating the dictionary")
print("===========================")
print("We can manipulate the data stored in a dictionary after declaration. This is shown in the example below.")
print(words) # print key-pairs
del words["Yes"] # delete a key-pair
print(words) # print key-pairs
words["Yes"] = "Oui" #add new key-pair
print(words)



"""
How i know how to code dictionaries
tests = {"test":50,
        "test2": 70,
        "test3": 65,
        "test4": 85}

print(tests["test"])
"""