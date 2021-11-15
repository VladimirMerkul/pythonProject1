arr = [1, 2, 3, 4, 5]
arr2 = []
for i in arr:
    arr2.insert(arr.index(i) -1, i)
print (arr2)