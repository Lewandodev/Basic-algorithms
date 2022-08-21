#liczby pierwsze
#liczba pierwsza to taka która dzieli się jedynie przez jeden i samą siebie



#najprostsza wersja algorytmu
def funkcja_czy_pierwsza(n):
    if n<=1:
        return False #sprawdzamy tylko dodatnie liczby + jeden nie jest liczbą pierwszą
    else:
        for i in range(2,n): #będziemy przechodzili przez wszystkie cyfry od 2 do do liczby poprzedzającą sprawdzaną (nie bierzemy pod uwagę n)
            if n%i==0:     #w celu wykluczenia potencjalnych dzielników innych niż 1 oraz nasza liczba
                return False #jeżeli znajdziemy inny dzielnik wiemy że liczba nie jest pierwsza
        return True

print('Czy 17 to liczba pierwsza?:',funkcja_czy_pierwsza(17))
print('\nBardziej wydajna wersja algorytmu 1:')
#powyższa wersja lagorytmu jest jednak mało wydajna w przypadku liczba składających się z wielu cyfr
#np.:dla liczby 81948157 algorytm będzie przechodził aż do cyfry 81948156 zabierając zbyt dużo czasu

#Bardziej wydajne wersje algorytmu:
#pierwsza wersja
def wydajana_funkcja_czy_pierwsza1(n):

    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1): #idziemy tylko do pierwiastka z n bo sqr(n)*sqr(n) to nadal n
        if n%i==0:                #pierwiastek z n jest swoistą "granicą" dzielników sprawdzanej liczby
            return False #aby lepiej zoobrazować rozłóżmy 16: 1*16,2*8,4*4(nasz pierwiastek z n),8*2,16*1 liczby za pierwiastkiem to to samo w innej kolejności
    return True                            #dla liczby która nie jest kwadratowa np: 18 pierwiastkową granicą byłoby sqr(18)*sqr(18)


print('czy 100000 jest liczbą pierwszą?:',wydajana_funkcja_czy_pierwsza1(100000))


print('Bardziej wydajna wersja algorytmu 2:')

#druga wersja
def wydajana_funkcja_czy_pierwsza2(n):
    if n<=1:
        return False
    if n==2:
        return True   #w drugiej wersji dodatkowo sprawdzamy czy wprowadzona liczba nie jest 2
    if n>2 and n%2==0: #oraz czy nie jest ona parzysta
        return False
    for i in range(3,int(n**0.5)+1,2): #sprawdzając dzielniki możemy przejść od 3 i skakać co 2 wykluczając wszystkie liczby parzyste
        if n%i==0:
            return False
    return True

print('czy 81948157 jest liczbą pierwszą?:',wydajana_funkcja_czy_pierwsza2(81948157))

print('\nzadanie z szukania w zakresie')

#Zadanie
def znajdź_liczby_pierwsze(zakres):
    zakresliczbowy = []
    for liczby in range(1,zakres):
        if wydajana_funkcja_czy_pierwsza1(liczby)==True:
            zakresliczbowy.append(liczby)
    return zakresliczbowy

print('liczby pierwsze w zakresie do 30:')
print(znajdź_liczby_pierwsze(30))


