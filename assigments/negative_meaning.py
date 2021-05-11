# Assignment - 3 (Negative Meaning)
# Complete the Code Challenge question. Good luck!

# 💡 Objective :
# To improve your defining function skills and string operations ability.


# Define a function to take a word and return negative meaning.
# Given a word, return a new word where "not " has been added to the front. 
# However, if the word already begins with "not", return the string unchanged.

# For example:

# Test	Result
# print(not_string('sugar'))
# not sugar
# print(not_string('x'))
# not x
# print(not_string('not bad'))
# not bad

def not_string(word):
    if word.find("not"):
        return "not " + word
    else:
        return word

print(not_string('sugar'))
print(not_string('x'))
print(not_string('not bad'))
