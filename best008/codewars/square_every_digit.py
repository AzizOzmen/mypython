def square_digits(num):
    return int("".join([str(i) for i in [(int(i)**2) for i in str(num)]]))
print(square_digits(9119))

