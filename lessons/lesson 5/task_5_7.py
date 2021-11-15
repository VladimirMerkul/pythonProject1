from random import randint
n=4
a=[]
p =0
x =0
for i in range(n):
    g=[]
    for v in range(n):
        v=randint(0,9)
        g.append(v)        
    a.append(g)
    m = max(g)
    for v in range(n):
        while x < n:
            if g[x] == m:
                x +=1
            else:
                g[x], m = m, g[x]
                x +=1
for i in a:
    print(i)  