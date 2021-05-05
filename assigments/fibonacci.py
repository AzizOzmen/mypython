#  Assignment-008/5 (Fibonacci Numbers) is due
# Wednesday, 5 May, 5:00 PM

# 💡Objective:
# To improve your control flow statement skills 
# and to raise your awareness of some algebraic knowledge.


# Task : Create a list consisting of Fibonacci numbers 
# from 1 to 55 using control flow statements.

# The desired output is like :

# fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

x = [1,1]
for i in range(1, 9):
    y = x[i-1]+x[i]
    x.append(y)
print(x)

f = 1
liste = []
for i in range(1,55):
    if i == 1:
        liste.append(f)
    else:
        liste.append(f)
        f = liste[-1] + liste[-2]
liste