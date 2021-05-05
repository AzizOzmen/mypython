# Exercise 17: Find words with both alphabets and numbers
# Given:

# str1 = "Emma25 is Data scientist50 and AI Expert"
# Expected Output:

# Emma25
# scientist50

# str1 = "Emma25 is Data 60 scientist50 and AI Expert"
# def keep_together(str):
#     str2 = str1.split()
#     for i in str2:
#         if 
#     print(str2)

# keep_together(str1)

str1 = "Emma25 is Data 60 scientist50 and AI Expert".split()
tog = []

for i in str1:
    for t in i:
        if t.isdigit():
            tog.append(i)
            break
for i in tog:
    for t in i:
        if t.isalpha():
            print(i)
            break    


str1 = "Emma25 is Data 60 scientist50 and AI Expert"
print("The original string is : " + str1)

# Words with both alphabets and numbers
# isdigit() for numbers + isalpha() for alphabets
# use any() to check each character

# res = []
# temp = str1.split()
# for item in temp:
#     if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
#         res.append(item)

# print("Displaying words with alphabets and numbers")
# for i in res:
#     print(i)