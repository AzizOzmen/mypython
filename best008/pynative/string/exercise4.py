# Exercise 4: Arrange string characters 
# such that lowercase letters should come first
# Given an input string with the combination of the lower 
# and upper case arrange characters in 
# such a way that all lowercase letters should come first.

# Given:
# str1 = PyNaTive
# Expected Output:

# yaivePNT

str1 = "PyNaTive"
my_list_L = []
my_list_u = []
for i in str1:
    if i.islower():
        my_list_L.append(i)
    else:
        my_list_u.append(i)
print(my_list_L)
print(my_list_u)
all_list = my_list_L+my_list_u
print(''.join(all_list))
    

