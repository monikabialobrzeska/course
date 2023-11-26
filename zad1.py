# Obliczanie dnia zwrotu butow od szewca
dzien_oddania_butów=int(input('W który dzień tygodnia oddasz buty do naprawy? '))
czas_trwania_naprawy=int(input('Ile dni potrwa naprawa butów? '))

# wprowadziłam dodatkowy warunek, ze naprawa nie moze potrwac wiecej niz 14 dni,
# bo nie wiem jak moznaby wprowadzic, ze byłoby to za 3 czy więcej tygodni
# tj nie wiem czy jest inny sposob niz wypisywanie w if, jesli dzien jest > niz i < niz.. do wszystkich przypadkow

if czas_trwania_naprawy>=14:
    print('Naprawa butów nie może trwac więcej niż 2 tygodnie')
    czas_trwania_naprawy = int(input('Ile dni potrwa naprawa butów? '))

dzien_odbioru=()
dzien_odbioru_butow = dzien_oddania_butów + czas_trwania_naprawy
print('Dzien_odbioru_butow: ', dzien_odbioru_butow)
input()
if dzien_odbioru_butow > 14:
    dzien_odbioru = dzien_odbioru_butow - 14
    print('Dzien_odbioru_butów:', dzien_odbioru, ', za dwa tygodnie.')
if dzien_odbioru_butow>7 and dzien_odbioru_butow<=14:
    dzien_odbioru = dzien_odbioru_butow - 7
    print('Dzien_odbioru_butów:', dzien_odbioru, 'w kolejnym tygodniu.')
if dzien_odbioru_butow<=7:
    dzien_odbioru = dzien_odbioru_butow
    print('Dzien_odbioru_butów:',dzien_odbioru, 'w tym tygodniu.')

dni_tygodnia_L=[1,2,3,4,5,6,7]
dni_tygodnia_S=['w poniedziałek','we wtorek','w środę','w czwartek','w piątek','w sobotę','w niedzielę']

for dzien in dni_tygodnia_L:
    if dzien_odbioru_butow>14:
        if dzien_odbioru == dzien:
            print(f'Buty będą do odebrania za dwa tygodnie  {dni_tygodnia_S[dzien - 1]}.')
    if dzien_odbioru_butow>7 and dzien_odbioru_butow<=14 :
        if dzien_odbioru == dzien:
            print(f'Buty będą do odebrania w kolejnym tygodniu {dni_tygodnia_S[dzien - 1]}.')
    if dzien_odbioru_butow <= 7:
        if dzien_odbioru == dzien:
            print(f'Buty będą do odebrania {dni_tygodnia_S[dzien-1]} w tym tygodniu.')



