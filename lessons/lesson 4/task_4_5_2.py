fib = []
a, b = 0,1
fib.append(a)
fib.append(b)
for a in fib:
        a, b = b, a + b
        fib.append (b)
        if len(fib)>14:
            break
print (fib)