# Exercise 6: Given a number count the total number of digits in a number
# For example, the number is 75869, so the output should be 5.

number = str(75869)
count = 0
# for i in number:
#     count += 1
# print(count) 

print([count:=count+1 for i in number][-1])

print(len([i for i in number]))

