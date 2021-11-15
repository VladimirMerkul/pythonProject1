from math import sqrt
    
limit = 300
pairs = {}
     
def divisors_sum(number):
    lst = []
    for x in range(1, int(sqrt(number))+1):
        if number%x == 0:
            if (number or x) != number//x:
                lst.append(x)
                lst.append(number//x)
            else:
                lst.append(1)
    return sum(lst)
    
for i in range(1, limit+1):
    aggr = divisors_sum(i)
    if i == divisors_sum(aggr) and i != aggr :
        if i not in pairs:
            pairs[i] = aggr
print (pairs)