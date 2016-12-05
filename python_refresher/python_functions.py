#!/usr/bin/env python

print("Functions")
print("---------")
print("A function is reusable code that can be called anywhere in your program. We use this syntax to define as function:")

function_lookie = '''
def function(parameters):
    instructions
    return value

The def keyword tells Python we have a piece of reusable code (A function). A program can have many functions.
Example: We can call the function using function(parameters)

def f(x):
    return x*x

print f(3)

The function has one parameter, x. The return value is the value the function returns.
Not all functions have to return something.
We can pass multiple variables:


Scope
-----
Variables can only reach the area in which they are defined, which is called scope.
This will not work

def f(x, y):
    print 'You called f(x,y) with the value x = ' + str(x) + ' and y = ' + str(y)
    print 'x * y = ' + str(x * y)
    z = 4  # cannot reach z, so THIS WON'T WORK


z = 3
f(3, 2)


But this will....


def f(x,y):
    z = 3
    print 'You called f(x,y) with the value x = ' + str(x) + ' and y = ' + str(y)
    print 'x * y = ' + str(x*y)
    print z # can reach because variable z is defined in the function

f(3,2)

Let's examine this further:

Calling functions in functions
------------------------------
We can also get the contents of a variable from another function:

def highFive():
    return 5

def f(x,y):
    z = highFive() # we get the variable contents from highFive()
    return x+y+z # returns x+y+z. z is reachable becaue it is defined above

result = f(3,2)
print result


A variable cannot be outside of the scope. The example below does not work
---------------------------------------------------------------------------

def doA():
a = 5

def doB():
    print a # does not know variable a, WILL NOT WORK!

doB()


But this example will...
-------------------------
def doA():
    a = 5

def doB(a):
    print a # we pass variable as parameter, this will work

doB(3)

In the last example we have two different variables named a, because the scope of the variable a is only within the function.
The variable is not known outside the scope.

The function doB() will print number 3 (the value passed to it).
The assignment a=5 is contained within function doA() and is never used and never visible to the function doB() or the rest of the code,
except within the function doA() itself.

If a variable can be reached anywhere in the code is called a global variable.
If a variable is known only inside the scope, we call it a local variable.
'''

print(function_lookie)

def f(x, y):
    print 'You called f(x,y) with the value x = ' + str(x) +  ' and y = ' + str(y)
    print 'x * y = ' + str(x*y)


f(3,2)

def f(x,y,z):
    return x+y+z

sum = f(3,2,1)
print(sum)


print "This is function calling - ", f(3,2,1)

print("\n")


def highFive():
    return 5


def f(x, y):
    z = highFive()  # we get the variable contents from highFive()
    return x + y + z  # returns x+y+z. z is reachable becaue it is defined above


result = f(3, 2)
print result