#!/usr/bin/env python

print ("In Python you can define conditional statements, known as if-statements. Consider this application:")
print
def smaller_bigger():
    x = 3
    if x < 10:
        print "x smaller than 10"
    else:
        print "x is bigger than or equal to 10"


smaller_bigger()


print ("If you set x to be larger than 10, it will execute the second code block.")
print ("We use indentation (4 spaces) to define the blocks.")
print
print ("A little game")
print ("A variable may not always be defined by the user, consider this litttle game: ")

print


def age_game():
    print("Guess my age, you have 1 chance!")
    guess = raw_input("Guess: ")
    age = '24'

    if guess != age:
        print ("Wrong!")
    else:
        print("Correct!")

age_game()
print("\n")
smaller_bigger()

print("\n")

print("Multiple Conditions")
print("The most straightforward way to do multiple conditions is nesting")
a = 9
b = 33

if a < 10:
    if b > 20:
        print("Good")

print("\n")


print("This can quickly become difficult to read, consider combining the 4 or 6 conditions. Luckily Python has a ")
print("solution for this, we can combine conditions using the and keyword")
print("Sometimes you may want to use the 'or' operator")
print("\n")

guess = 24
if guess > 10 and guess <20:
    print("In range")
else:
    print("Out of range")