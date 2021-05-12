# Exercise 4: Print multiplication table of a given number
# For example, num = 2 so the output should be

# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

# number = int(input("Enter a number: "))
# for i in range(1,11):
#     print(number*i)


for i in range(1,11):
    print("")
    for j in range(1,11):
        print("{:<3}".format(i*j), end=" ")
print()

for i in range(1,11):
    print("")
    for j in range(1,11):
        print("{:>2}".format(i*j), end=" ")
 