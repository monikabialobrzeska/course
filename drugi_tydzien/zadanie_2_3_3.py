#Program podaje liczbę zawodników dla każdego kraju

from funkcje_do_zad2_3 import przetwarzanie_danych

# Otwarcie pliku CSV i wczytanie danych
with open('zawodnicy.csv', mode='r', encoding='UTF-8') as file:
    lines = file.readlines()

# Przetwarzanie danych do obliczania statystyk :)
skoczkowie = [przetwarzanie_danych(linia) for linia in lines]

#Stworzenie listy ul
unikalne_kraje = set()
for skoczek in skoczkowie:
    unikalne_kraje.add(skoczek['kraj'])
liczba_krajow = len(unikalne_kraje)
print('--------------------------------------------------------------------------------------------------------------')
print(f'Liczba różnych krajów: {liczba_krajow}.\nSą to: {unikalne_kraje}')

# Liczenie wystąpień poszczególnych krajów
licznik_krajow = {}

for skoczek in skoczkowie:
    kraj = skoczek['kraj']
    if kraj in licznik_krajow:
        licznik_krajow[kraj] += 1
    else:
        licznik_krajow[kraj] = 1

# Posortowanie krajów alfabetycznie
posortowane_kraje = sorted(licznik_krajow.keys())

# Wyświetlenie wyników
print('Liczba skoczków z poszczególnych krajów (posortowane alfabetycznie):')
for kraj in posortowane_kraje:
    liczba_skoczkow = licznik_krajow[kraj]
    print(f'{kraj}: {liczba_skoczkow} skoczków')
