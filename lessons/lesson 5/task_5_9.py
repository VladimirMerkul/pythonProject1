numb = int(input('Введите начальное число: '))
numb2 = int (input('Введите конечное число:'))
while numb <= numb2:    
    for i in range(numb - 1, 1, -1):
        if (numb % i == 0):
            print(numb, ':',  i, end = " ")
    numb+=1