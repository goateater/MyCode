#!/usr/bin/env python

import random

print("Python Lists")

l = ["Drake", "Derp", "Derek", "Dominique"]
print(l)
print(l[0])
print(l[1])
print(l[0:3])

print("\n")

print("Sort list - We can sort the list using the sort() function")
print(l)
l.sort()
print(l)
l.reverse()
print(l)
random.shuffle(l)
print(l)

print("\n")

print("Append and remove list items")
print(l)
l.append("Victoria")
print(l)
l.remove("Derp")
l.remove("Drake")
print(l)



a = ['james','make','susan']
a.reverse()
print(a)


list = [[0, 1, 4], [1, 2, 5], [2, 3, 6]]
print(list)
print(list[0][0])
print(list[1][2])