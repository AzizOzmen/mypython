# Assignment-008/4 (Is it a Prime Number?) is due
# Sunday, 2 May, 5:00 PM

# 💡Objective:
# To improve your control flow statement skills 
# and to raise your awareness of some algebraic knowledge.
# Write your Python codes on any IDLE, 
# push it up to your GitHub repository 
# and submit your GitHub Page link address in addition to your code as a plain text.

# Task : Write a program that takes a number from the user 
# and prints the result to check if it is a prime number.

# The examples of the desired output are as follows :

# input →  19 ⇉ output : 19 is a prime number
# input →  10 ⇉ output : 10 is not a prime number
# Note that ⚠: This question is famous on the web, 
# so to get more benefit from this assignment, 
# try to complete this task on your own. 

number = input("Enter a number: ")
i = 2
if number.isdigit():
    number = int(number)
    while number > i:
        if number % i == 0:
            print(f"{number} is not a prime number")
            break
        else:
            i += 1
    if i == number:
        print(f"{number} is a prime number")
else:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")

print("Josephs answer")

n = int(input("Enter a number to check if it is a prime number."))
count = 0
for i in range(1, n+1) :
    if n % i == 0 :
        count += 1
if (n == 0) or (n == 1) or (count >=3) :
    print(n, "is not a prime number.")
else:
    print(n, "is a prime number")