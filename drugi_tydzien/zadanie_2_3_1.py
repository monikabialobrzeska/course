from funkcje_do_zad2_3 import przetwarzanie_danych, oblicz_statystyki

# Otwarcie pliku CSV i wczytanie danych
with open('zawodnicy.csv', mode='r', encoding='UTF-8') as file:
    lines = file.readlines()

# Przetwarzanie danych do obliczania statystyk :)
skoczkowie = [przetwarzanie_danych(linia) for linia in lines]

# Użycie funkcji do obliczania statystyk dla wszystkich krajów, printowanie dla mnie dodatkowo, żebym widziała, co i jak się wyświetla
statystyki = oblicz_statystyki(skoczkowie)
print('---------------------------------------------------------------------------------------------------------------')
print('statystyki: ',statystyki)

# Wyświetlenie wyników
print(f'W pliku skoczkowie.csv jest {statystyki['liczba_skoczkow']} zawodników z {statystyki['liczba_krajow']} krajów')
print('')
print(f'Średni wzrost wszystkich zawodników: {statystyki['sredni_wzrost']:.2f} cm')
print(f'Suma wag wszystkich zawodników: {statystyki['suma_wag']} kg')
print(f'Najwyższy zawodnik: {statystyki['najwyzszy']['imie']} {statystyki['najwyzszy']['nazwisko']} - Wzrost: {statystyki['najwyzszy']['wzrost']} cm')
print(f'Najniższy zawodnik: {statystyki['najnizszy']['imie']} {statystyki['najnizszy']['nazwisko']} - Wzrost: {statystyki['najnizszy']['wzrost']} cm')
print(f'Najcięższy zawodnik: {statystyki['najciezszy']['imie']} {statystyki['najciezszy']['nazwisko']} - Waga: {statystyki['najciezszy']['waga']} kg')
print(f'Najlżejszy zawodnik: {statystyki['najlzejszy']['imie']} {statystyki['najlzejszy']['nazwisko']} - Waga: {statystyki['najlzejszy']['waga']} kg')
