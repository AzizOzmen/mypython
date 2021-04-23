num = int(input("please enter number of number you will enter: "))
list = []
max = 0
for i in range(1, num + 1):
  list.append((int(input("Please enter the {}. number: ".format(i)))))
for i in list:
  if i > max:
    max = i
  else:
    continue
print("The largest number is : ",max)
