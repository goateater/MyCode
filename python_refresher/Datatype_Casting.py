#!/usr/bin/env python

print("Datatype Casting")
print("================")
print("To convert between datatypes you can use: ")
print("Function \t\t\tDescription" )
print("======== \t\t\t==========")
print("int(x)\t\t\tConverts x to an integer" )
print("long(x)\t\t\tConverts x to a long integer")
print("float(x)\t\tConverts x to a floating point number" )
print("str(x)\t\t\tConverts x to an string.  x can be of the type float. integer or long." )
print("hex(x)\t\t\tConverts x integer to a hexadecimal string" )
print("chr(x)\t\t\tConverts x integer to a character" )
print("ord(x)\t\t\tConverts character x to an integer" )

print("\n")


print("An example of casting datatypes in Python")
print("If you want to print numbers you will often need casting.")
print("In this example below we want to print two numbers, one whole number (integer) and one floating point number.")
print("=========================================")
x = 3
y = 2.15315315313532

print ("We need to have defined two numbers")
print "x = " + str(x)
print "y = " + str(y)

a = "135.31421"
b = "133.1112223"

c = a + b
print c
c = float(a) + float(b)
print c