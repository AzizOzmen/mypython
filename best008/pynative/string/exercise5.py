# Exercise 5: Count all lower case, upper case, digits, 
# and special symbols from a given string

# Given:
# str1 = "P@#yn26at^&i5ve"
# Expected Outcome:
# Total counts of chars, digits,and symbols 

# Chars = 8 
# Digits = 3 
# Symbol = 4

str1 = "P@#yn26at^&i5ve"
lower_l = [] 
upper_l = []
digits_l = []
symbol_l = []
for i in str1:
    if i.islower():
        lower_l.append(i)
    elif i.isupper():
        upper_l.append(i)
    elif i.isdigit():
        digits_l.append(i)
    else:
        symbol_l.append(i)
print(len(lower_l))
print(len(upper_l))
print(len(digits_l))
print(len(symbol_l))


text = "gdkri551fg@d&"
d = {"Char" : 0, "Digit" : 0, "Symbol" : 0}
for i in text:
    if i.isdigit():
        d["Digit"] += 1 
    elif i.isupper() or i.islower():
        d["Char"] += 1
    else:
        d["Symbol"] += 1
print(d)


