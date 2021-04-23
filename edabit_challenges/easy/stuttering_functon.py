# Write a function that stutters a word as if someone is struggling to read it. 
# The first two letters are repeated twice with an ellipsis ... 
# and space after each, and then the word is pronounced with a question mark ?.

# Examples
# stutter("incredible") ➞ "in... in... incredible?"

# stutter("enthusiastic") ➞ "en... en... enthusiastic?"

# stutter("outstanding") ➞ "ou... ou... outstanding?"

def stutter(word):
    print(word[0:2] + '... ' + word[0:2] + '... ' + word + "?")

stutter("incredible") 
stutter("enthusiastic") 
stutter("outstanding") 
