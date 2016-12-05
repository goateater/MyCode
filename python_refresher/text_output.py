#!/usr/bin/env python

s = "Hello Python"
print(s)

#name = raw_input("Enter name: ")
#print(name)

sentence = "The cat is brown"
q = "cat"

if q == sentence:
    print("strings are equal")

print(s)
print(s[0])
print(s[1])

print(s[0:2])
print(s[2:4])
print(s[6:])

print("str.replace(old, new, max)")
print("The method replace returns a new string with old replaced by new")
print("The format is str.replace(old, new, max)")
print("Parameters: string: The string to be replaced  new: The string to be used  max:  Maximum amount of replacements.Leave blank for infinite.")
s = "All work and no play makes Jack a dull boy. Jack?"
s = s.replace("Jack", "Joe")
print(s)

print("\n")

print("capitalize(str):")
print("the method capitalize returns a new string with first letter capitalized.")
str = "the capitalize method returns the string with first letter capitalized."
print(str.capitalize())

print("\n")

print("count(str)")
print("Return the number of substrings in string:")
print("The format is str.count(sub) or str.count(sub,start.end)")
str = "The string count method returns the number of sub string occurences. "
print(str.count("string"))

print("\n")

print("find(str)")
print("Return the index of a substring (if found). Returns -1 if not found.")
print("The format is str.find(string) or str.find(string,start,end)")
print("Parameters: string: The string to search  start: Index to start searching(optional)  end: Ending index(optional)")
str = "Tip of the day"
print( str.find("day"))

print("\n")

print("index(str)")
print("Return the index of a substring (if found). Returns exception if not found.")
print("The format is str.index(string) or str.index(string,start,end)")
print("Parameters: string: The string to search  start: Index to start searching(optional)  end: Ending index(optional)")
str = "Tip of the day"
print( str.index("Tip"))
#print( str.index("Tip",5))


print("\n")


print("len(str)")
print("The format is len(str)")
str = "All work and no play makes Jack a dull boy. Jack?"
strlen = len(str)
print(strlen)


print("\n")

print("str.isdecimal()")
print("Return True if string is decimal")
print("The format is str.decimal()")
"""
The method isdecimal() checks whether the string consists of only decimal characters.
This method are present only on unicode objects.
Note: To define a string as Unicode, one simply prefixes a 'u' to the opening quotation mark of the assignment.
Below is the example.
"""
str = u"1.234" #
print (str.isdecimal())
str = u"12345"
print (str.isdecimal())

print("\n")

print("str.isdigit()")
print("Return True if string consists only of digits")
print("The format is str.isdigit()")
str = u"string digit 1234"
print(str.isdigit())
str = u"12345"
print(str.isdigit())

print("\n")

print("str.isnumeric()")
print("Return True if string is numeric")
print("The format is str.numeric()")
str = u"someone speak python here? sssss"
print(str.isnumeric())
str = u"12345"
print(str.isnumeric())

print("\n")


print("str.lower()")
print("Returns string in lowercase")
print("The format is str.lower()")

s = "All work and no play makes Jack a dull boy. Jack?"
print(s)
s = s.lower()
print(s)

print("\n")

print("str.upper()")
print("Returns string in uppercase")
print("The format is str.upper()")
s = "All work and no play makes Jack a dull boy. Jack?"
print(s)
s = s.upper()
print(s)


print("\n")


print("Escape Characters")
str1 = "In Python,\nyou can use special characters in strings.\nThese special characters can be..."
print(str1)
str1 = "The word \"computer\" will be in quotes"
print(str1)
str1 = "The word \"quotes\" will be tabbed \tquotes"
print(str1)
str1 = "The word \"quotes\" will have a backslash in front of it \\quotes"
print(str1)
