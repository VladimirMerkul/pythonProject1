s = str (input ('введите почту'))
a1 = str (s [-9:])
a = str ('gmail.com')
if  a == a1:
    print (s)
else:
    print ('DOMAIN NAME is not supported')