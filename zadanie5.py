from random import randint
wylosowana_liczba = randint(0, 999)
proba=0
zgadywana_liczba=int(input('Zgadnij jaka to liczba: ? '))

while zgadywana_liczba!=wylosowana_liczba:
    if zgadywana_liczba > wylosowana_liczba:
        print('Zła odpowiedź. Ta liczba jest za duża !!')
        proba += 1
        zgadywana_liczba=int(input('Spróbuj jeszcze raz. Podaj mniejszą liczbę: ? '))
    elif zgadywana_liczba < wylosowana_liczba:
        print('Zła odpowiedź. Ta liczba jest za mała !!')
        proba += 1
        zgadywana_liczba=int(input('Spróbuj jeszcze raz. Podaj większą liczbę: ? '))
proba+=1
print(f'Prawidłowa odpowiedz !! Zgadłes  za {proba} razem. Gratulacje !!! ')
