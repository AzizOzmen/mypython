# Exercise 16: Removal all the characters 
# other than integers from a string
# Given:

# str1 = 'I am 25 years and 10 months old'
# Expected Output:

# 2510

str1 = 'I am 25 years and 10 months old'

def rem_str(str):
    digit = ""
    for i in str:
        if i.isdigit():
            digit += i
    print(digit)

rem_str(str1)

str1 = 'I am 25 years and 10 months old'
print("Original string is", str1)

# Retain Numbers in String
# Using list comprehension + join() + isdigit()
res = "".join([item for item in str1 if item.isdigit()])

print(res)

