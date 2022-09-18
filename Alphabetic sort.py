#algorytm polega na sortowaniu alfabetycznym zbioru wyrażeń, kolejne wyrazy wrzucamy na odpowiednie miejsce w liście
#potrzebujemy 2 funckji

#algorithm is based on sorting an array of different words in alphabetical order, next words will be put on correct places of list
#we will need 2 functions

#polski
def czy_zamiana(wyr1,wyr2):

    if len(wyr1)<=len(wyr2):
        for i in range(0,len(wyr1)):
            if ord(wyr1[i])>ord(wyr2[i]):
                return True
            if ord(wyr1[i])<ord(wyr2[i]):   #sprawdzamy jeżlei np w wyr1 jest A a w wyr 2 litera D
                return False                #to nie robimy zamiany ascii A mniejsze od D i alfabetycznie większe od D

        return False

    if len(wyr1)>len(wyr2):
        for i in range(0,len(wyr2)):
            if ord(wyr1[i])>ord(wyr2[i]):
                return True
            if ord(wyr1[i])<ord(wyr2[i]):
                return False
        return True

#porządkowanie odbywa się przy pomocy sortowania bąbelkowego z użytą uwcześnie funkcją sprawdzającą wartości ASCII liter

def uporządkuj(ciągznaków):
    for i in range(0,len(ciągznaków)):              #!!!!!!WAŻNE!!!!!!
        for j in range(0,len(ciągznaków)): #podczas korzystania z sortowania bąbelkowego nie pomijamy ostatniego indeksu ani nie odejmujemy i
            if czy_zamiana(ciągznaków[j],ciągznaków[i]):
                pomocnicza=ciągznaków[i]
                ciągznaków[i]=ciągznaków[j]
                ciągznaków[j]=pomocnicza

    return ciągznaków

print('Porządkowanie alfabetyczne ciągu słów')
ciag=['DEF', 'DEFAAAA', 'ZBC', 'ABC', 'AABD']
print(ciag)
print(uporządkuj(ciag))


print('\nPorządkowanie alfabetyczne unikalnych znaków w słowie w odwrotnej kolejności ')
print('Sortowanie liter słowa "kajak" w odwrotnej kolejności:')
def porządkowanie(wyrazenie):
    for i in range(0,len(wyrazenie)):
        for j in range(len(wyrazenie)):
            if czy_porządk(wyrazenie[j],wyrazenie[i])==False:
                pom=wyrazenie[i]
                wyrazenie[i]=wyrazenie[j]
                wyrazenie[j]=pom
    return wyrazenie

def czy_porządk(wyraz1,wyraz2):

    if len(wyraz1)<=len(wyraz2):
        for i in range(0,len(wyraz1)):
            if ascii(wyraz1[i])>ascii(wyraz2[i]):
                return True
            if ascii(wyraz1[i])<ascii(wyraz2[i]):
                return False

        return False

    if len(wyraz1)>len(wyraz2):
        for i in range(0,len(wyraz2)):
            if ascii(wyraz1[i])>ascii(wyraz2[i]):
                return True
            if ascii(wyraz1[i])<ascii(wyraz2[i]):
                return False

        return True

def odwrt(wyrazenie):
    lista=[]
    for i in range(0,len(wyrazenie)):
        if wyrazenie[i] not in lista:
            lista.append(wyrazenie[i])

    porządkowanie(lista)
    return lista

print(odwrt('kajak'))


