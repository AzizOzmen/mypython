# Exercise 10: Given an input string, 
# count occurrences of all characters within a string

# Given:
# str1 = "Apple"
# Expected Outcome:
# {'A': 1, 'p': 2, 'l': 1, 'e': 1}

str1 = "Apple"
dic = {}
for i in str1:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1
print(dic)

