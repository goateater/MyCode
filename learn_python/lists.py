print "Lists"
print "Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables " \
      "as you wish. Lists can also be iterated over in a very simple manner. Here is an example of how to build a list."


mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)

print("\n")

print "Using the slicing method to print out each object in the list"
print(mylist[0])
print(mylist[1])
print(mylist[2])

print("\n")

print "Using a for loop to print out each object in the list"
for x in mylist:
    print(x)
print("\n")



numbers = [] # Empty list
strings = [] # Empty list
names = ["John", "Eric", "Jessica"]
numbers.append(1) # Adding to the numbers list
numbers.append(2) # Adding to the numbers list
numbers.append(3) # Adding to the numbers list
strings.append("hello")  # Adding to the strings list
strings.append("world")  # Adding to the strings list
#numbers.append(2)
#numbers.append(3)
# write your code here
second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

print "Hello"
print ("Hello")
