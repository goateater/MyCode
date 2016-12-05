#!/usr/bin/env python


from random import *
print random()


print("Random numbers")
print("Using the random module, we can generate pseudo-random numbers. The function random() generates a random number "
      "between zero and one [0,0.1 .. 1]. Numbers generated with this module are not truly random but they are enough "
      "random for most purposes.")

print("Random number between 0 and 1")
print("We can generate a (pseudo) random floating point number with this small code.")
print("\n")
print("Genrate random number between 1 and 100")
print("To generate a whole number (integer) between one and one hundred use")
print random.randint(1,100)