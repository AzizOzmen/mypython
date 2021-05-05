# Exercise 15: Remove special symbols/Punctuation from a given string
# Given:

# str1 = "/*Jon is @developer & musician"
# Expected Output:

# "Jon is developer musician"
str1 = "/*Jon is @developer & musician"
# def remove_symbol(str):
#     symbol = []
#     new_str1 = str1.split()
#     print(new_str1)
#     for i in new_str1:
#         print(i, end="")
#         for j in i:
#             print(j, end="")
#             if i.isalpha():
#                 symbol.append(i)
#                 x= "".join(symbol)
#     print(x)

# remove_symbol(str1)
from string import punctuation
strr = "/*Jon is @developer &musician".split()
new_str = ""
for i in strr:
    for y in punctuation:
        if y in i:
            print(i)
            i = i.strip(punctuation)
            # i = i.replace(punctuation,"")
    new_str += i + " "
new_str = new_str.strip()
print(new_str)

# import string

# str1 = "/*Jon is @developer & musician"
# print("Original string is ", str1)

# # use translate function of a string
# # and maketrans function of str class
# new_str = str1.translate(str.maketrans('', '', string.punctuation))

# print("New string is ", new_str)

# import re

# str1 = "/*Jon is @developer & musician"
# print("Original string is ", str1)

# str2 = re.sub(r'[^\w\s]', '', str1)
# print("New string is also ", str2)