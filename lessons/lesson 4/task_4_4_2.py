arr = [1, 2, 3, 4, 5]
arr2 = []
i = 1
while len(arr)!=len(arr2):
    arr2.insert(arr.index(i) -1, i)
    i = i+1
print (arr2)