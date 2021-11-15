s = str (input ('введите строку'))

if (len (s)%2 >0):
    print (s [(len (s)//2)] )
else:
    print ('четная строка')
    
if  (s[(len (s)//2)] == s[0]):
    print (s [1:-1])
else:
    pass