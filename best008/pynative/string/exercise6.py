# Exercise 6: Given two strings, s1 and s2, 
# create a mixed String using the following rules
# Note: create a third-string made of the first char of s1 
# then the last char of s2, Next, the second char of s1 and 
# second last char of s2, and so on. 
# Any leftover chars go at the end of the result.

# Given:

# s1 = "Abc"
# s2 = "Xyz"
# Expected Output:
# AzbycX

def mixString(s1, s2):
  s2 = s2[::-1]
  lengthS1 = len(s1)
  lengthS2 = len(s2)
  length  = lengthS1 if lengthS1 > lengthS2 else lengthS2
  resultString=""
  for i in range(length):
    if(i < lengthS1):
      resultString = resultString + s1[i]
    if(i < lengthS2):
      resultString = resultString + s2[i]
  print(resultString)
s1 = "Abc"
s2 = "Xyz"
mixString(s1, s2)

s1 = "Abc"
s2 = "Xyz"
print(s1)
s2n= s2[::-1]
print(s2n)
new = []
while True:
    for i in s1:
        new.append(i)
        for k in s2n:
            if s1.index(i) == s2.index(i):
                print("new.append(k)")
            else:
                print("hi")
            
print(new)


