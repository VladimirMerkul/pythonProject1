a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
h=[]
i = 0
while i < len(a):
    number = (a[i]* (-2))
    i += 1
    h.append(int(number))
print(h) 