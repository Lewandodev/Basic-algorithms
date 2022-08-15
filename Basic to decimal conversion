#Algorithm marked by me for recision after I comes back from vacation some things will be changed
print('---Zamiana liczby z dowolnego systemu na system decymalny---')
print('-------Zamiana z dowolnego na decymalny --------')
def cyfra(n):
    if n==str(n):
        s=int(n,16)
        return s
    if n>=0 and n<10:
        return n        #zwróć n zrzutowane na typ liczbowy

def zamiana_kazdego_na_decymalny(liczba,system_liczby):
    liczba = str(liczba)
    potega=0
    nowa_wartosc=0

    k=len(liczba)
    for i in range(k-1,-1,-1):
        nowa_wartosc = nowa_wartosc + cyfra((liczba[i]))*system_liczby**potega
        potega+=1
    return nowa_wartosc

print(zamiana_kazdego_na_decymalny('100011',2))
print(zamiana_kazdego_na_decymalny('1001111',2))
print(zamiana_kazdego_na_decymalny('61',8))
print(zamiana_kazdego_na_decymalny('8D',16))
print(zamiana_kazdego_na_decymalny('321',4))

print('---------Zadanie 2 ponizej---------------')
#Zad 2

def potęgowanie(liczba,potęga):
    if potęga==0:
        return 1
    elif potęga==1:
        return liczba
    else:
        return liczba*potęgowanie(liczba,potęga-1)


def cyrfa(n):
    if n==str(n):
        s=int(n,16)
        return s
    if n>=0 and n<10:
        return n

def dowolny_na_decymalny(dowolna_liczba,system_liczby):
    przetrzymywana=0
    potęga=0
    dowolna_liczba=str(dowolna_liczba)
    dl_licz=len(dowolna_liczba)

    for i in range(dl_licz-1,-1,-1):
        przetrzymywana=przetrzymywana+cyrfa(dowolna_liczba[i])*potęgowanie(system_liczby,potęga)
        potęga+=1
    return przetrzymywana

print(dowolny_na_decymalny('100011',2))
print(dowolny_na_decymalny('1001111',2))
print(dowolny_na_decymalny('61',8))
print(dowolny_na_decymalny('8D',16))
print(dowolny_na_decymalny('321',4))

