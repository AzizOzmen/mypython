# Assignment-008/6 (Prime Numbers)

# 💡Objective:
# To improve your control flow statement skills 
# and to raise your awareness of some algebraic knowledge.
# Write a Python code on any IDE, 
# push it up to your GitHub repository 
# and submit the GitHub page address link 
# in addition to your code (answer) as a plain text.

# Task : Print the prime numbers which are between 1 to entered limit number (n).

# You can use a nested for loop.
# Collect all these numbers into a list
# The desired output for n=100 :

# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
# 61, 67, 71, 73, 79, 83, 89, 97]
# Note that : This question is famous on the web, 
# so to get more benefit from this assignment, 
# try to complete this task on your own.



n = int(input("Enter an end point to check prime numbers: "))
prime_numbers = []
for i in range(1, n+1) :
    count = 0
    for j in range(1, i+1):
        if i % j == 0 :
            count += 1
    if (i == 0) or (i == 1) or (count >=3) :
        continue
    else:
        prime_numbers.append(i)
print(prime_numbers, "are prime numbers")