fib = []
a, b = 0,1
counter = 0
fib.append(a)
fib.append(b)
while counter < 13:
        a, b = b, a + b
        counter +=1
        fib.append (b)
print (fib)
        