#liczby pierwsze


def funkcja_czy_pierwsza(n):
    if n<=1:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True

print(funkcja_czy_pierwsza(17))
print('---------------')

#Bardziej wydajne wersje algorytmu:
#pierwsza wersja idziemy tylko do pierwiastka z n bo sqr(n)*sqr(n) to nadal n, a zapobiegamy duplikacji np 18=6*3 i 3*6 to to samo tylko w innej kolejnosci
def wydajana_funkcja_czy_pierwsza1(n):

    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
print(wydajana_funkcja_czy_pierwsza1(100000))
print('--------------------1 wersja wydajniejszego algorytmu powyzej-------')

#druga wersja
def wydajana_funkcja_czy_pierwsza2(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n>2 and n%2==0: #jezeli n jest parzyste i n nie jest równe dwa nie jest liczbą pierwszą
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

print(wydajana_funkcja_czy_pierwsza2(81948157))

print('--------------------- 2 wersja bardziej wydajnego algorytmu powyżej-----------')

#Zadanie
def znajdź_liczby_pierwsze(zakres):
    zakresliczbowy = []
    for liczby in range(1,zakres):
        if wydajana_funkcja_czy_pierwsza1(liczby)==True:
            zakresliczbowy.append(liczby)
    return zakresliczbowy

print(znajdź_liczby_pierwsze(30))

print('--------zadanie z szukania w zakresie wyzej-----------')
