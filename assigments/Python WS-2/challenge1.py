size = input("How many numbers do you have? ")
size = int(size)
num_list = []
for i in range(size):
    numbers = int(input("Enter a number: "))
    num_list.append(numbers)
    sorted_list = sorted(num_list)
print(num_list)
print(sorted_list[-1])
