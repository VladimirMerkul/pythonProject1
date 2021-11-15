from pprint import pprint
from random import randint

n = 4
m = 5

arr = []
for i in range(n):
    arr1 = []
    for j in range(m):
        p = randint(0, 9)
        arr1.append(p)
    arr.append(arr1)
sum = 0
count = 0
for i in range(n):
    for j in range(m):
        sum += arr[i][j]
        count += 1
aver = sum/count
print (arr)
print(aver)


