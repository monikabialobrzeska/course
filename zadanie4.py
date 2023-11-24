#cennik
gipsowanie=100 #za 1m2 sciany
malowanie=30 #za metr2
panele=50 #za m2 podłogi
listwy=40 #za metr bieżacy

dlugosc_A=int(input('podaj dlugosc pokoju: '))
szerokosc_B=int(input('podaj szerokosc pokoju: '))
wysokosc=int(input('podaj wysokosc pokoju: '))
pow_scianyA=dlugosc_A*wysokosc
pow_scianyB= szerokosc_B*wysokosc
pow_podlogi_sufitu=dlugosc_A*szerokosc_B
obwod_pokoju=2*dlugosc_A + 2*szerokosc_B

print(f'dlugosc_A: {dlugosc_A} m, szerokosc_B: {szerokosc_B} m, wysokosc: {wysokosc} m, pow_scianyA: {pow_scianyA} m2, pow_scianyB {pow_scianyB} m2, pow_podlogi_sufitu {pow_podlogi_sufitu} m2, obwód pokoju: {obwod_pokoju} m')
gipsowanie_scian=gipsowanie*(2*pow_scianyA+2*pow_scianyB)
malowanie_scian_i_sufitow=malowanie*(2*pow_scianyA+2*pow_scianyB+pow_podlogi_sufitu)
kladzenie_paneli_podlogowych=panele*pow_podlogi_sufitu
kladzenie_listw=listwy*obwod_pokoju

print('gipsowanie ścian', gipsowanie_scian, 'pln')
print('malowanie ścian i sufitów', malowanie_scian_i_sufitow, 'pln')
print('polozenie paneli podlogowych', kladzenie_paneli_podlogowych, 'pln')
print('położenie listew przypodłogowych', kladzenie_listw, 'pln')

print('-----------------------------------------------------------------------------------------------------')
suma=0
pytanie1=str(input('Czy gipsować ściany?: '))
pytanie2=str(input('Czy malowac ściany?: '))
pytanie3=str(input('Czy kłasc panele podłogowe?: '))
pytanie4=str(input('Czy kłaśc listwy przypodłogowe?: '))

if pytanie1.upper()=='TAK':
    suma+=gipsowanie_scian
else: suma=suma
if pytanie2.upper()=='TAK':
    suma+=malowanie_scian_i_sufitow
else: suma=suma
if pytanie3.upper()=='TAK':
    suma+=kladzenie_paneli_podlogowych
else: suma=suma
if pytanie4.upper()=='TAK':
    suma+=kladzenie_listw
else: suma=suma
print('Całośc prac:',suma)



