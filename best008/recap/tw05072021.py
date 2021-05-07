def Max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')

Max(3, 4)

x = 50
y = 10
def func(x):
    print('x is', x)
    x = 2
    global y
    print("y is:", y)
    y = 30
    print('Changed local x to', x)

func(x)
print('x is now', x)
print("y is now global:", y)


def function1(var1=5, var2=7):
    var2=9
    var1=3
    print (var1, " ", var2)
function1(10,12)