print ('уравнение ах**2+bx+c=0')
a = int ( input('введите а'))
b = int ( input('введите b'))
c = int ( input('введите c'))
D = (b**2 -4*a*c)
if D < 0:
    print ('нет корней')
else:
    if D == 0:
        x = (-(b)+sqrt(D))/(2*(a))
        print ('x=' + (x))
    else:
        x1 = (-(b)+sqrt(D))/(2*(a))
        x2 = (-(b)-sqrt(D))/(2*(a))
        print ('x1=' + (x1))
        print ('x2=' + (x2))