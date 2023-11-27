from random import randint,choice, choices

# nie umiałam stworzyc planszy dwuwymiarowej o wymiarach 10 na 10
# rozwiązałam to zadanie okrężną drogą
# nie miałam innego pomysłu
# nie wiem jak dodac informację o tym, czy zmierza w dobrym kierunku.
# mozliwe, ze przy tej okreznej drodze sie nie da...

lista_liczb=list(range(1, 101)) # od 1 do 100
#print('lista liczb', lista_liczb)
print('plansza do gry:')
print(lista_liczb[0:10])
print(lista_liczb[10:20])
print(lista_liczb[20:30])
print(lista_liczb[30:40])
print(lista_liczb[40:50])
print(lista_liczb[50:60])
print(lista_liczb[60:70])
print(lista_liczb[70:80])
print(lista_liczb[80:90])
print(lista_liczb[90:100])

pozycja_skarbu=choice(lista_liczb)
pozycja_gracza=choice(lista_liczb)
print('pozycja skarbu', pozycja_skarbu)
print('pozycja gracza', pozycja_gracza)

ruch=input('Gdzie idziesz? :')
ile_prob=1
while pozycja_gracza!=pozycja_skarbu:
    if ruch=='gora':
        pozycja_gracza=pozycja_gracza-10
        if pozycja_gracza not in lista_liczb:
            print('Jestes poza planszą. PRZEGRAŁES :( !!! ')
            break
        else:
            print('Nowa pozycja_gracza', pozycja_gracza)
            if pozycja_gracza!=pozycja_skarbu:
                ruch = input('Gdzie idziesz? :')
                ile_prob+=1
            else:
                print(f'Znalazles skarb !! Pozycja gracza {pozycja_gracza} jest taka sama jak lokalizacja skarbu {pozycja_skarbu}. ')
                print(f'Udało Ci się znaleźc skarb w {ile_prob} krokach. Gratulacje !!')
    if ruch=='dol':
        pozycja_gracza = pozycja_gracza + 10
        if pozycja_gracza not in lista_liczb:
            print('Jestes poza planszą. PRZEGRAŁES :( !!! ')
            break
        else:
            print('Nowa pozycja_gracza', pozycja_gracza)
            if pozycja_gracza != pozycja_skarbu:
                ruch = input('Gdzie idziesz? :')
                ile_prob += 1
            else:
                print(f'Znalazles skarb !! Pozycja gracza {pozycja_gracza} jest taka sama jak lokalizacja skarbu {pozycja_skarbu}. ')
                print(f'Udało Ci się znaleźc skarb w {ile_prob} krokach. Gratulacje !!')
    if ruch=='prawo':
        pozycja_gracza = pozycja_gracza + 1
        print('Nowa pozycja gracza:', pozycja_gracza)
        if (pozycja_gracza-1) % 10==0:
            print('Jestes poza planszą. PRZEGRAŁES :( !!! ')
            break
        else:
            print('Nowa pozycja_gracza', pozycja_gracza)
            if pozycja_gracza != pozycja_skarbu:
                ruch = input('Gdzie idziesz? :')
                ile_prob += 1
            else:
                print(f'Znalazles skarb !! Pozycja gracza {pozycja_gracza} jest taka sama jak lokalizacja skarbu {pozycja_skarbu}. ')
                print(f'Udało Ci się znaleźc skarb w {ile_prob} krokach. Gratulacje !!')
    if ruch=='lewo':
        pozycja_gracza = pozycja_gracza - 1
        print('Nowa pozycja gracza:', pozycja_gracza)
        if (pozycja_gracza-2) % 10 == 9:
            print('Jestes poza planszą. PRZEGRAŁES :( !!! ')
            break
        else:
            if pozycja_gracza != pozycja_skarbu:
                ruch = input('Gdzie idziesz? :')
                ile_prob += 1
            else:
                print(f'Znalazles skarb !! Pozycja gracza {pozycja_gracza} jest taka sama jak lokalizacja skarbu {pozycja_skarbu}. ')
                print(f'Udało Ci się znaleźc skarb w {ile_prob} krokach. Gratulacje !!')
print('KONIEC GRY :)')
