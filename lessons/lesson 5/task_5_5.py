arr = [3, 5, 7, 8, 15, 71, 86, 24, 27, 15, 82, 28, 57, 24, 12, 15, 17, 36, 22]
max_number = max (arr)
x = 0
for x in arr:
    while x <=18:    
        if arr[(int(x))] % 2 == 0:
            arr[x] = max_number
        x +=1
print (arr)
    