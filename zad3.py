liczba_calkowita=int(input('liczba całkowita: '))

for i in range(1,liczba_calkowita+1):
    gwiazdki='*'*(2*i-1)
    spacje = ' ' * (liczba_calkowita - i)  # Dodaj spacje przed gwiazdkami
    print(spacje + gwiazdki)

# komentarz dla mnie, łatwiej zrozumiałe :) 
# dla 3
# dla 1 gwiazdki='*' * (2*1-1)=1, a spacje=' ' * (3-1)=2
# dla 2 gwiazdki='*' * (2*2-1)=3, a spacje=' ' * (3-2)
# dla 3 gwiazdki='*' * (2*3-1)=5, a spacje=' ' * (3-3)

# dla 5
# dla 1 gwiazdki='*' * (2*1-1)=1, a spacje=' ' * (5-1)
# dla 2 gwiazdki='*' * (2*2-1)=3, a spacje=' ' * (5-2)
# dla 3 gwiazdki='*' * (2*3-1)=5, a spacje=' ' * (5-3)
# dla 4 gwiazdki='*' * (2*4-1)=7, a spacje=' ' * (5-4)
# dla 5 gwiazdki='*' * (2*5-1)=9, a spacje=' ' * (5-5)
