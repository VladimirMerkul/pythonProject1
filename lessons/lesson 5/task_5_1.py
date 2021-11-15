s = str (input('для продолжения введите любой знак, для остановки 0'))
while s != ('0'):
    x = int (input ('введите первое число'))
    y = int (input ('введите второе число'))
    z = str (input ('введите действие(+-*/)'))
    if z == ('+') or z == ('-') or z == ('*') or z == ('/'):
        if y == 0 and z == str ('/'):
             print ('на 0 делить нельзя')
        else:
            if z == str ('+'):
                a = x + y
                print (a)
            else:
                if z == str ('-'):
                    a = x - y
                    print (a)
                else:
                    if z == str ('/'):
                        a = x / y
                        print (a)
                    else:
                        if z == str ('*'):
                            a = x * y
                            print (a)       
    else:
        print ('неверное действие')         
    s = str (input('для продолжения введите любой знак, для остановки 0'))