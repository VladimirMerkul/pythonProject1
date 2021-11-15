a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
i = 0
c = 0
while i < len(a):
    if a[i] % 2 == 0:
        c+=1
    else:
        pass
    i +=1
print(c)