#!/usr/bin/env python

intro = '''
In Python and many other programming languages you can repeat a part of code using a loop.
 A loop repeats a set of instructions N times. Python has 3 loops:

Type:           Description:
For            Executes the defined statements until the condition is met
While          Executes the defined statements while a condition is true.
Nested loops   Loops inside loops.
 '''

print(intro)

print("Python 'For' loop example")
print("We can iterate a list using a for loop")
print("\n")

items = ["Abby", "Brenda", "Cindy", "Diddy"]

for item in items:
    print item, (type(item))

print("\n")
print("The for loop can be used to repeat N times too: ")
for i in range(1,10):
    print(i)

print("\n")
print("Python While loop example")
print("Until a condition is met we can repeat some instructions, For example,")

#while button_not_pressed:
 #   drive()

print("Nested Loops in Python")
print("We can combine for loops using nesting. If we want to iterate over an (x,y) field we could use")
for x in range(1,10):
    for y in range(1,10):
        print "(" + str(x) + "'" + str(y) + ")"

print("Nesting is very useful, but it increases complexity the deeper you nest.")