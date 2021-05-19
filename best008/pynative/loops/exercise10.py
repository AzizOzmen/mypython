# Exercise 10: Display a message “Done” after successful execution of for loop
# For example, the following loop will execute without any error.

# for i in range(5):
#     print(i)
# So the Expected output should be:

# 0
# 1
# 2
# 3
# 4
# Done!

for i in range(5):
    print(i)
print("Done!")

print("\n".join(str(i) for i in range(5)), "\nDone!")

for i in range(5):
    print(i)
else:
    print("Done!")