# Q1
a=[1,2,3,4]
b=[sum(a[0:x+1]) for x in range(0,len(a))]
print(b)
# Answer [1, 3, 6, 10]

# Q2
L1 = []
print(L1)
L1.append([1, [2, 3], 4])
print(L1, f'type: {type(L1)} len: {len(L1)}')
L1.extend([7, 8, 9])
print(L1, f'type: {type(L1)} len: {len(L1)}')
print(L1[0][1][1] + L1[2], f'type: {type(L1)} len: {len(L1)}')
print(L1[0][1][1], f'type: {type(L1)} len: {len(L1)}')
print(L1[2], f'type: {type(L1)} len: {len(L1)}')
# Answer 11 

# Q3
T = (1, 2, 3, 4, 5, 6, 7, 8)
print(T[T.index(5)], end = " ")
print(T[T[T[6]-3]-6])
# Answer 5 8

# Q4
D = {1 : 1, 2 : '2', '1' : 1, '2' : 3}
D['1'] = 2
print(D)
print(str(D[1]))
print(D[D[D[str(D[1])]]])
# Answer

set1 = {1, 2, 3}
set2 = set1.copy()
set2.add(4)
print(set1)
print(set2)