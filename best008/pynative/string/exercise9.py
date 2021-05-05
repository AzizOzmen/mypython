# Exercise 9: Given a string, 
# return the sum and average of the digits 
# that appear in the string, ignoring all other characters

# Given:
# str1 = "English = 78 Science = 83 Math = 68 History = 65"

# Expected Outcome:
# sum is 294
# average is 73.5

import math
str1 = "English = 78 Science = 83 Math = 68 History = 65"

new_list = str1.split(" ")
my_list = []
for i in new_list:
    if i.isdigit():
        my_list.append(int(i))
print(my_list)
print(f" sum {sum(my_list)}")
print(f" avarage {sum(my_list)/len(my_list)}")

