# Exercise 8: Find all occurrences of “USA” 
# in a given string ignoring the case

# Given:
# str1 = "Welcome to USA. usa awesome, isn't it?"

# Expected Outcome:
# The USA count is: 2

str1 = "Welcome to USA. usa awesome, isn't it?".upper()
print(str1.count("USA"))