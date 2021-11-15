def inch_sm():
    inch = float (input ('Введите дюймы для перевода в сантиметры'))
    sm = inch * 2.5
    print (sm)

def sm_inch():
    sm = float (input ('Введите сантиметры для перевода в дюймы'))
    inch = sm / 2.5
    print (inch)

def mile_km():
    mile = float (input ('Введите мили для перевода в километры'))
    km = mile * 1.6
    print (km)

def km_mile():
    km = float (input ('Введите километры для перевода в мили'))
    mile = km /1.6
    print (mile)

def funt_kg():
    funt = float (input ('Введите фунты для перевода в килограммы'))
    kg = funt * 0.45
    print (kg)

def kg_funt():
    kg = float (input ('Введите килограммы для перевода в фунты'))
    funt = kg / 0.45
    print (funt)

def ozz_gr():
    ozz = float (input ('Введите унции для перевода в граммы'))
    gr = ozz * 0.035
    print (gr)

def gr_ozz():
    gr = float (input ('Введите граммы для перевода в унции'))
    ozz = gr / 0.035
    print (ozz)

def gl_lt():
    gl = float (input ('Введите галлоны для перевода в литры'))
    lt = gl * 3.78
    print (lt)

def lt_gl():
    lt = float (input ('Введите литры для перевода в галлоны'))
    gl = lt / 3.78
    print (gl)

def pint_lt():
    pint = float (input ('Введите пинты для перевода в литры'))
    lt = pint * 0.568
    print (lt)

def lt_pint():
    lt = float (input ('Введите пинты для перевода в литры'))
    pint = lt / 0.568
    print (pint)

print ('Для перевода дюймов в сантиметры введите 1'
       'Для перевода сантиметров в дюймы введите 2'
       'Для перевода миль в километры введите 3'
       'Для перевода километров в мили введите 4'
       'Для переаода фунтов в килограммы введите 5'
       'Для перевода килограммов в фунты введите 6'
       'Для перевода унций в граммы введите 7'
       'Для перевода граммов в унции введите 8'
       'Для перевода галлоноа а литры введите 9'
       'Для перевода литров в галлонв ведите 10'
       'Для перевода пинт в литры введите 11'
       'Для перевода литров в пинты введите 12'
       'Для завершения введите 0')
x = int(input('Введите действие'))
while x != 0:

    if x == 1:
        inch_sm()

    if x == 2:
        sm_inch()

    if x == 3:
        mile_km()

    if x == 4:
        km_mile()

    if x == 5:
        funt_kg()

    if x == 6:
        kg_funt()

    if x == 7:
        ozz_gr()

    if x == 8:
        gr_ozz()

    if x == 9:
        gl_lt()

    if x == 10:
        lt_gl()

    if x == 11:
        pint_lt()

    if x == 12:
        lt_pint()

    y = int(input('Введите действие'))
    x = y