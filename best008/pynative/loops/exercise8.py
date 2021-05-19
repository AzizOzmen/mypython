# Exercise 8: Reverse the following list using for loop
# list1 = [10, 20, 30, 40, 50]

list1 = [10, 20, 30, 40, 50]
list1.reverse()
for i in list1:
    print(i)
 
print("\n".join(str(i) for i in list1))
