# Exercise 13: Write a loop to find the factorial of any number
# The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

# For example: calculate the factorial of 5

# 5! = 5 × 4 × 3 × 2 × 1 = 120
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)


print(factorial(5))

