arr = [3, 5, 7, 8, 15, 71, 86, 24, 27, 15, 82, 28, 57, 24, 12, 15, 17, 36, 23]
x = 0
l = len (arr)
counter = 0
for x in arr:
     if x <= (l -1) and arr[x] < arr[(x)+1]:
         x += 1
     else:
         counter += 1
print (counter)
    