# Basic Calculator
# Create a function that takes two numbers 
# and a mathematical operator + - / * 
# and will perform a calculation with the given numbers.

# Examples
# calculator(2, "+", 2) ➞ 4
# calculator(2, "*", 2) ➞ 4
# calculator(4, "/", 2) ➞ 2

import operator
def calculator(x, f, y):
    if y == 0 and f == "/":
        print("Can't divide by 0!")
    else:
        op = {'+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
         '/': lambda x, y: x / y
         }
        print(op[f](x, y))
calculator(2, "+", 2)
calculator(2, "*", 2) 
calculator(4, "/", 2)
calculator(4, "/", 0)