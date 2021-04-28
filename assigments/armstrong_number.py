# Find out if a given number is an "Armstrong Number".

# An n-digit number that is the sum of the nth powers of its digits 
# is called an n-Armstrong number. Examples :
# 371 = 33 + 73 + 13;
# 9474 = 94 + 44 + 74 + 44;
# 93084 = 95 + 35 + 05 + 85 + 45.

# Write a Python program that;
# takes a positive integer number from the user,
# checks the entered number if it is Armstrong,
# consider the negative, float and any entries 
# other than numeric values then display a warning message to the user.

# Examples
# Sample inputs	Outputs
# 407       407 is an Armstrong number
# 5         5 is an Armstrong number
# -153	    It is an invalid entry. Don't use non-numeric, float, or negative values!
# 153.87    or 153,87	 It is an invalid entry. Don't use non-numeric, float, or negative values!
# one	    It is an invalid entry. Don't use non-numeric, float, or negative values!
# 121	    121 is not an Armstrong number
while True:
    number = input("Enter a number: ")
    if number.isdigit() and int(number) > 0: # or not(type(number) is int)):
        number_list = list(number)
        exp = len(number)
        sum_number = 0
        for i in number_list:
            sum_number += int(i) ** exp
        if sum_number == int(number):    
            print(f"{number} is an Armstrong number.")
        else:
            print(f"{number} is not an Armstrong number.")
        new_check = input("If would you like to check an other number enter 'yes': ")
        new_check = new_check.lower()
        if new_check == "yes":
            continue
        else:
            print("See you next time, thank you")
            break
    else: 
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")


