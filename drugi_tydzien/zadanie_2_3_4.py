# Program, ktory printuje statystyki dla wsystkich krajow

from funkcje_do_zad2_3 import przetwarzanie_danych,oblicz_statystyki_dla_kraju

# Otwarcie pliku CSV i wczytanie danych
with open('zawodnicy.csv', mode='r', encoding='UTF-8') as file:
    lines = file.readlines()

# Przetwarzanie danych do obliczania statystyk :)
skoczkowie = [przetwarzanie_danych(linia) for linia in lines]
unikalne_kraje = set()
for skoczek in skoczkowie:
    unikalne_kraje.add(skoczek['kraj'])
print('--------------------------------------------------------------------------------------------------------------')
print('Kraje: ',unikalne_kraje)
print('--------------------------------------------------------------------------------------------------------------')

for wybrany_kraj in unikalne_kraje:
    statystyka = oblicz_statystyki_dla_kraju(skoczkowie, wybrany_kraj)
    print(f'W pliku skoczkowie.csv jest {statystyka['Liczba_skoczkow']} zawodników z {wybrany_kraj}')
    print(f'Średni wzrost wszystkich zawodników z {wybrany_kraj}: {statystyka['Sredni_wzrost_zawodnikow']:.2f} cm')
    print(f'Suma wag wszystkich zawodników z {wybrany_kraj}: {statystyka['Suma_wag_zawodnikow']} kg')
    print(
        f'Najwyższy zawodnik z {wybrany_kraj}: {statystyka['Najwyzszy_zawodnik']['imie']} {statystyka['Najwyzszy_zawodnik']['nazwisko']} - Wzrost: {statystyka['Najwyzszy_zawodnik']['wzrost']} cm')
    print(
        f'Najniższy zawodnik z {wybrany_kraj}: {statystyka['Najnizszy_zawodnik']['imie']} {statystyka['Najnizszy_zawodnik']['nazwisko']} - Wzrost: {statystyka['Najnizszy_zawodnik']['wzrost']} cm')
    print(
        f'Najcięższy zawodnik z {wybrany_kraj}: {statystyka['Najciezszy_zawodnik']['imie']} {statystyka['Najciezszy_zawodnik']['nazwisko']} - Waga: {statystyka['Najciezszy_zawodnik']['waga']} kg')
    print(
        f'Najlżejszy zawodnik z {wybrany_kraj}: {statystyka['Najlzejszy_zawodnik']['imie']} {statystyka['Najlzejszy_zawodnik']['nazwisko']} - Waga: {statystyka['Najlzejszy_zawodnik']['waga']} kg')
    print('-----------------------------------------------------------------------------------------------------------')
