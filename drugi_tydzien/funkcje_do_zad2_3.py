# Pomocnicza funkcja do obrobki danych,wskazanie separatora, wyprintowanie danych (dla mnie :)
# W tej funkcji tworzony jest slownik zawierający przetworzone dane skoczków - klucze to nazwy kolumn, a wartości to odpowiednie dane.

def przetwarzanie_danych(linia):
    data = linia.strip().split(';')
    print('data: ', data)
    imie, nazwisko, kraj, data_urodzenia, wzrost, waga = data
    return {'imie': imie, 'nazwisko': nazwisko, 'kraj': kraj, 'data_urodzenia': data_urodzenia, 'wzrost': int(wzrost), 'waga': int(waga)}


def oblicz_statystyki(skoczkowie):
    liczba_skoczkow = len(skoczkowie)
    liczba_krajow = len(set(skoczek['kraj'] for skoczek in skoczkowie))

    sredni_wzrost = sum(skoczek['wzrost'] for skoczek in skoczkowie) / liczba_skoczkow
    suma_wag = sum(skoczek['waga'] for skoczek in skoczkowie)

    najwyzszy = max(skoczkowie, key=lambda x: x['wzrost'])
    najnizszy = min(skoczkowie, key=lambda x: x['wzrost'])

    najciezszy = max(skoczkowie, key=lambda x: x['waga'])
    najlzejszy = min(skoczkowie, key=lambda x: x['waga'])

    wyniki = {
        'liczba_skoczkow': liczba_skoczkow,
        'liczba_krajow': liczba_krajow,
        'sredni_wzrost': sredni_wzrost,
        'suma_wag': suma_wag,
        'najwyzszy': najwyzszy,
        'najnizszy': najnizszy,
        'najciezszy': najciezszy,
        'najlzejszy': najlzejszy,
    }

    return wyniki


def oblicz_statystyki_dla_kraju(skoczkowie, wybrany_kraj):
    skoczkowie_kraju = [skoczek for skoczek in skoczkowie if skoczek['kraj'] == wybrany_kraj]

    liczba_skoczkow = len(skoczkowie_kraju)

    if liczba_skoczkow == 0:
        print(f'Brak danych dla wybranego kraju: {wybrany_kraj}')
        return None

    sredni_wzrost = round(sum(skoczek['wzrost'] for skoczek in skoczkowie_kraju) / liczba_skoczkow, 2)
    suma_wag = sum(skoczek['waga'] for skoczek in skoczkowie_kraju)

    najwyzszy = max(skoczkowie_kraju, key=lambda x: x['wzrost'])
    najnizszy = min(skoczkowie_kraju, key=lambda x: x['wzrost'])

    najciezszy = max(skoczkowie_kraju, key=lambda x: x['waga'])
    najlzejszy = min(skoczkowie_kraju, key=lambda x: x['waga'])

    wyniki = {
        'Liczba_skoczkow': liczba_skoczkow,
        'Sredni_wzrost_zawodnikow'.format(wybrany_kraj): sredni_wzrost,
        'Suma_wag_zawodnikow'.format(wybrany_kraj): suma_wag,
        'Najwyzszy_zawodnik'.format(wybrany_kraj): najwyzszy,
        'Najnizszy_zawodnik'.format(wybrany_kraj): najnizszy,
        'Najciezszy_zawodnik'.format(wybrany_kraj): najciezszy,
        'Najlzejszy_zawodnik'.format(wybrany_kraj): najlzejszy,
    }


    return wyniki
