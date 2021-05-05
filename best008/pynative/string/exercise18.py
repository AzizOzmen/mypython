# Exercise 18: Replace each punctuation with # in the following string
# Given:

# str1 = '/*Jon is @developer & musician!!'
# Expected Output:

# ##Jon is #developer # musician##

# import string library function 
import string 
    
# An input string.
Sentence = "Hey, Geeks !, How are you?"
  
for i in Sentence:
      
    # checking whether the char is punctuation.
    if i in string.punctuation:
          
        # Printing the punctuation values 
        print("Punctuation: " + i)


str1 = '/*Jon is @developer & musician!!'
from string import punctuation
def add_hash(str):
    for i in str:
        if i in string.punctuation:
            print(i)
            print(punctuation)

add_hash(str1)

str1 = '/*Jon is @developer & musician!!'.split()
specials = "/*@&!.,;"
new_str = []
for i in str1:
    for j in i:
        if  j  in specials:
            i = i.replace(j, "#")
    new_str.append(i)
print(" ".join(new_str))

from string import punctuation

str1 = '/*Jon is @developer & musician!!'
print("The original string is : ", str1)

# Replace punctuations with #
replace_char = '#'

# Using string.punctuation to get the list of all punctuations
# use string function replace() to replace each punctuation with #

for char in punctuation:
    str1 = str1.replace(char, replace_char)

print("The strings after replacement : ", str1)

