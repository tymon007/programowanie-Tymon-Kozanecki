from random import randint
liczba = randint(1, 100)
proba = 0
while True:
    proba += 1
    ja = int(input('Podaj liczbe od 1 do 100: '))
    if liczba == ja:
        print(f' Odgadłeś liczbe po {proba} probach')
        break
    elif ja < liczba:
        print('za malo')
    else:
        print('za duzo')