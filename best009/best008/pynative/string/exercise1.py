# Exercise 1: Given a string of odd length greater than 7, 
# return a new string made of 
# the middle three characters of a given String

my_string = input("Enter a string: ")
print(my_string[len(my_string)//2-1]+\
    my_string[len(my_string)//2]+\
        my_string[len(my_string)//2+1])

my_string = input("Enter a string: ")
middle = len(my_string)//2
print(my_string[middle-1:middle+2])