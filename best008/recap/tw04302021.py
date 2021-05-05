fruits = {'Apples': 5, 'Oranges': 3, 'Bananas': 4}
fruit_names = [x for x in fruits.keys()]
print(fruit_names)
fruit_names = (x for x in fruits.keys())
print(* fruit_names)

i = 5
while True:
    if i%0O11 == 0:
        break
    print(i)
    i += 1

x = ["abcd"]
for i in range(len(x)):
    x = x[i].upper()
    print (x)

x = ["a","b","c","d"]
for i in range(len(x)):
    x[i]=x[i].upper()
print(x)

k=[2,3,4]

print("-----")
l = reversed(k)
print(* l)
m = list(reversed(k))
print(m)
print("-----")

list1 = [2,3,4]
list1.reverse()
print (list1)


k=[2,3,4]
x=reversed(k)
y=list(reversed(k))
print(*x)
print(y)