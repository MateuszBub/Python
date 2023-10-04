import random

chars = 'abcdefghijklmnoprstwyzxABCDEFGHIJKLMNOPRSTWYZX123456789!@#$%^&*'

ilosc = input('Podaj ilosc : ')
ilosc = int(ilosc)


dlugosc = input('Podaj dlugosc : ')
dlugosc = int(dlugosc)

print('tutaj sa twoje hasla')

for hasło in range(ilosc):
    hasła = ''
    for c in range(dlugosc):
     hasła += random.choice(chars)
    print (hasła)