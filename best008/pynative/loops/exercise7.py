# Exercise 7: Print the following pattern using for loop
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end = " ")
    print()

# print(" ".join("\n".join([str(j) for i in range(5, 0, -1)]) for j in range(i, 0, -1)))

# print(" ".join(str(i) for i in range(j, 0, -1) for j in range(5, 0, -1)))