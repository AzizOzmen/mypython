# Exercise 9: How to check file is empty or not
import os
# import best008\pynative\test.txt
print(os.stat("test.txt").st_size == 0)