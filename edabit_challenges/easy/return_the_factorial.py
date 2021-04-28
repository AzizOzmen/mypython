# Return the Factorial
# Create a function that takes an integer 
# and returns the factorial of that integer. 
# That is, the integer multiplied by all positive lower integers.
# Notes
# Assume all inputs are greater than or equal to 0.

# Examples
# factorial(3) ➞ 6
# factorial(5) ➞ 120
# factorial(13) ➞ 6227020800

def factorial(number):
    numbers_in_list = []
    for i in range(1,number+1):
        numbers_in_list.append(i)
        result = 1
        for j in numbers_in_list:
            result = j * result 
    print(result)
        
factorial(3)
factorial(5)
factorial(13)