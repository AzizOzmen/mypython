# Exercise 7: String characters balance Test
# We’ll assume that a String s1 and s2 is balanced 
# if all the chars in the s1 are there in s2. characters’ position doesn’t matter.

# Given:
# Case 1:
# s1 = "Yn"
# s2 = "PYnative"
# Expected Output:
# True

# Case 2:
# s1 = "Ynf"
# s2 = "PYnative"
# Expected Output:
# False

s1 = "Ynf"
s2 = "PYnative"
cond = True
for i in s1:
    if i in s2:
        continue
    else:
        cond = False
if cond:
    print("True")
else:
    print("False")


s1 = "Yn"
s2 = "PYnative"
if s1 in s1:
    print("True")
else:
    print("False")