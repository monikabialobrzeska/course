from math import *
from random import randint

# napisz program, który odczytuje 3 liczby i sprawdza, czy mogą byc bokami trójkąta, dla mnie określenie troche ogólne,
# nie do końca rozumiem, czy te liczby mają byc w jakims zakresie itd
# dlatego zrobione są rozne wersje zadania :)


# 1 wersja : użytkownik podaje liczby
print('Wersja 1')
a=int(input('podaj pierwszą liczbę: '))
b=int(input('podaj drugą liczbę: '))
c=int(input('podaj trzecią liczbę: '))
print('Program teraz sprawdzi czy te liczby mogą byc bokami trójkąta.......')

if a+b>c and a+c>b and b+c>a:
    print('Wybrane liczby MOGĄ byc bokami trójkąta')
    obwod=a+b+c
    polowa_obwodu = (a + b + c) / 2
    pole_Wzor_Herona = sqrt(polowa_obwodu * (polowa_obwodu - a) * (polowa_obwodu - b) * (polowa_obwodu - c))
    print(f'Obwód trójkąta o bokach {a},{b},{c} wynosi {obwod}, więc połowa to: {polowa_obwodu}. Pole tego trójkąta to: {pole_Wzor_Herona:.4f}')
else:
    print('Wybrane liczby NIE MOGĄ byc bokami trójkąta, bo dlugosci boków nie spełniają warunków')

print('------------------------------------------------------------------------------------------')
input('Naciśnij Enter, aby wyświetlic wersję 2')
print('Wersja 2')
# 2 wersja : program losuje liczby z zakresu 1 do 10
a1 = randint(1,10)
b1 = randint(1,10)
c1 = randint(1,10)
print(f'pierwsza wylosowana liczba: {a1}, druga wylosowana liczba: {b1}, trzecia wylosowana liczba: {c1}')
print('Program teraz sprawdzi czy wylosowane liczby mogą byc bokami trójkąta.......')
if a1+b1>c1 and a1+c1>b1 and b1+c1>a1:
    print('Wylosowane liczby MOGĄ byc bokami trójkąta')
    obwod1= a1 + b1 + c1
    polowa_obwodu1 = (a1 + b1 + c1) / 2
    pole_Wzor_Herona1 = sqrt(polowa_obwodu1 * (polowa_obwodu1 - a1) * (polowa_obwodu1 - b1) * (polowa_obwodu1 - c1))
    print(f'Obwód trójkąta o wylosowanych bokach {a1},{b1},{c1} wynosi {obwod1}, więc połowa to: {polowa_obwodu1}. Pole takiego trójkąta to: {pole_Wzor_Herona1:.4f}')
else:
    print('Wybrane liczby NIE MOGĄ byc bokami trójkąta, bo długosci boków nie spełniają warunków')

print('------------------------------------------------------------------------------------------')
input('Naciśnij Enter, aby wyświetlic wersję 3')
print('Wersja 3')
#dla ciekawosci sprobowalam dorzucic dodatkowe zadanie, zeby program losował do momentu znalezienia wlasciwych liczb
#losowanie z zakresu 1 do 20

a2 = randint(1, 100)
b2 = randint(1, 100)
c2 = randint(1, 100)
print(f'Pierwsza wylosowana liczba {a2}, druga wylosowana liczba {b2}, trzecia wylosowana liczba {c2}. Program teraz sprawdzi czy wylosowane liczby mogą byc bokami trójkąta.......')

while a2+b2<c2 or a2+c2<b2 or b2+c2<a2:
    print(f'Wylosowane liczby {a2},{b2}, {c2} nie mogą byc bokami trójkąta, bo dlugosci boków nie spełniają warunków.')
    a2 = randint(1, 100)
    b2 = randint(1, 100)
    c2 = randint(1, 100)
input('Losuj kolejne liczby !!!')
print(f'Super. Nowe liczby: {a2}, {b2}, {c2} mogą byc bokami trójkąta.')
obwod2= a2 + b2 + c2
polowa_obwodu2 = (a2 + b2 + c2) / 2
pole_Wzor_Herona2 = sqrt(polowa_obwodu2 * (polowa_obwodu2 - a2) * (polowa_obwodu2 - b2) * (polowa_obwodu2 - c2))
print(f'Obwód trójkąta o bokach {a2},{b2},{c2} wynosi {obwod2}, więc połowa to: {polowa_obwodu2}. Pole takiego trójkąta to: {pole_Wzor_Herona2:.4f}')
