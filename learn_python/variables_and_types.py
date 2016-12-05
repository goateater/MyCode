# change this code  -- variables
mystring = 'hello'
myfloat = 10.0
#myfloat = float(10)
myint = 20

# testing code using Strings
if mystring == "hello":
    print "String: %s" % mystring
if isinstance(myfloat, float) and myfloat == 10.0:
    print "Float: %d" % myfloat
if isinstance(myint, int) and myint == 20:
    print "Integer: %d" % myint


mystring2 = "Don't worry about apostrophes"

one = 1
two = 2
three = one + two
print three
print("\n")
hello = 'hello'
world = 'world'
helloworld = hello + " " + world

print hello
print world
print helloworld
print mystring2


a, b = 3, 4
print (a,b)

# This will not work
#print one + two + hello

# This will work
print one, two, hello

