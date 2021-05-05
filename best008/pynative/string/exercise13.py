# Exercise 13: Split a given string on hyphens into several substrings and display each substring
# Given:

# str1 = Emma-is-a-data-scientist
# Expected Output:

# Displaying each substring

# Emma
# is
# a
# data
# scientist

str1 = "Emma-is-a-data-scientist"
def split_str(str):
    str2 = str.split("-")
    for i in str2:
        print(i)

split_str(str1)

