print('Ben', 25, 'California', sep='--')
print('[%c]' % 65)
x= '(%c)' % (255)
print(type(x))

x = float('NaN')
print('%f, %e, %F, %E' % (x, x, x, x))


for x in set('pqr'):
    print(x*2)

d = {}
d = {"john":40, "peter":45}
d = {40:"john", 45:"peter"}

d = {"john":40, "peter":45}
print(d["john"])

d = {"john":40, "peter":45}
print(list(d.keys()), type(list(d.keys())))

a={}
a['a']=1
a['b']=[2,3,4]
print(a)

z=set('abc')
print(z)
z.add('san')
print(z)
z.update(set(['p', 'q']))
print(z)

num_people = 5
if num_people > 10:
    print("There is a lot of people in the pool.")
elif num_people > 4:
    print("There are some people in the pool.")
elif num_people > 0:
    print("There are a few people in the pool.")
else:
    print("There is no one in the pool.")

if num_people > 10:
    print("There is a lot of people in the pool.")
if num_people > 4:
    print("There are some people in the pool.")
if num_people > 0:
    print("There are a few people in the pool.")
else:
    print("There is no one in the pool.")

num_people = 5
if num_people > 10:
    print("There is a lot of people in the pool.")
elif num_people > 4:
    print("There are some people in the pool.")
elif num_people > 0:
    print("There are a few people in the pool.")
else:
    print("There is no one in the pool.")

count, fruit, price = (2, 'apple', 3.5)

college_years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
print(list(enumerate(college_years, 2019)))

