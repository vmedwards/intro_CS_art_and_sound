"""
Author: Victoria Edwards
Date: 04/14/2026
Course: ES1098

Description: Conditionals 
"""

# 04/14/2026
# String comparision
v = "voyager"
e = "v"
# TEST 1 
print("String Conditions")
if e in v: 
    print("True: " + e + " is in " + v)
else:
    print("False: " + e + " is not in " + v)

# Test 2
if v in e: 
    print("True: " + v + " is in " + e)
else:
    print("False: " + v + " is not in " + e)


# Test 3 

# Test if the strings are the same
v = "Test"
e = "Test"
e = "test"
if v is e: 
    print("True: " + e + " is " + v)
else: 
    print("False: " + e + " is not " + v)

e = "Test"
if v == e: 
    print("True: " + e + " is " + v)
else: 
    print("False: " + e + " is not " + v)


# Test 4
v = "class A"
e = "class A"
# Test if the strings are not the same
if v is not e: 
    print("True: " + e + " is not " + v)
else: 
    print("False: " + e + " is " + v)

e = "Class B"
if v != e: 
    print("True: " + e + " is not " + v)
else: 
    print("False: " + e + " is " + v)


# Test 5

# Test the type of a variable

v = 21
#v = "21"
if type(v) is str: 
    print("Type is a string")
else:
    print("Not string")


# Numeric comparision
# Test 1

# compare number values
print("Number tests")
# Test 1
x = 10
y = 5
if x >= y: 
    print("X: " + str(x) + " is geq " + str(y))
else: 
    print("False")

# Test 2
# using elif 
x = 15
y = 5
if x == y: 
    print("X equals Y")
elif x > y: 
    print("X bigger than Y")
else: 
    print("X is smaller than Y")


# Test 3

# Does order matter?

x = 5
y = 5
if x >= y: 
    print("X equals Y")
elif x == y:
    print("X bigger than Y")
else: 
    print("X the same or smaller than Y")

x = 20
if x > 3: 
    print(x)
elif x > 5: 
    print(5)
elif x > 10: 
    print("WHY")
else: 
    print("all other cases ")



# Test 4
# Check for all even numbers between 0 and 20 and print even or odd




"""
# get numbers from 0 to 20 
for i in range(21):
    # check if even
    print(i / 2)
    #if ( i // 2 - i / 2 ) == 0.0: 
    if i // 2 == i / 2: 
        # print even 
        print(str(i) + " is Even ")
    # check if odd 
    else:
        # print odd 
        print(str(i) + " is Odd")

# Does this solution answer the question?
for i in range(1, 21, 2):
    print(i)
"""
