# Exercise 11: Write a program to display all prime numbers within a range
# Note: A Prime Number is a whole number that cannot be made by multiplying other whole numbers

# Examples:

# 6 is not a Prime Number because it can be made by 2×3 = 6
# 37 is a Prime Number because no other whole numbers multiply together to make it.
# Given:

# start = 25
# end = 50
# Expected output:

# Prime numbers between 25 and 50 are:
# 29
# 31
# 37
# 41
# 43
# 47


for i in range(25, 51):
    count = 0
    for j in range(2, i):
        if i % j == 0:
            count += 1 
    if count >= 1:
        continue
        print(i, "Prime Degil")
    else:
        print(i, "Prime!")


# list = []
# for i in range(25, 51):
#     for j in range(2, i+1):
#         if (i % i == 0 and i % 1 == 0 and i % j == 0):
#             list.append(j)
#             if len(list) >= 1:
#                 print(i, "Prime Degil")
                
#         else:
#             print(i, "Prime")

for i in range(25, 50):
    for j in range(2, i):
        if(i % j==0):
            break
    else:
        print(i, "Prime")

num = int(input("Please provide a number: "))
for i in range(2, num):
    if num % i == 0:
        print("{} is not a prime number". format(num))
        break
else:
    print("{} is a prime number". format(num))



