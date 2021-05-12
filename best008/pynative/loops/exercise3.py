# Exercise 3: Accept number from user 
# and calculate the sum of all number from 1 to a given number
# For example, if user entered 10 the output should be 55.

number = int(input("Enter a number: "))
x = 0
for i in range(number+1):
    x += i
print(x)

number = int(input("Enter a number: "))
print(sum([i for i in range(number+1)]))

total = 0
[total := total + x for x in range(13)]
print("total", total)

