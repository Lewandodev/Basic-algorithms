print('------Sprawdzanie czy liczba jest doskonała zadania ponizej------')
#Sprawdzanie czy liczba jest doskonała
#1 Algorytm
def czy_doskonała(n):
    suma_dzielników=0
    dzielniki=[]
    for i in range(1,(n//2)+1):
        if n%i==0:
            dzielniki.append(i)

    for cyfyr_dzielników in dzielniki:
        suma_dzielników+=cyfyr_dzielników
    if suma_dzielników==n:
        return True
    else:
        return False

print(czy_doskonała(8128))

print('----1 algorytm z dzielników i sprawdzania czy liczba jest doskonała powyżej------')
#Zad 2

def znajdź_liczby_doskonałe(zakres):
    lista_doskonałych=[]
    for cyfry in range(1,zakres+1):
        if czy_doskonała(cyfry)==True:
            lista_doskonałych.append(cyfry)
    return lista_doskonałych

print(znajdź_liczby_doskonałe(100))

print('-----------------Zadanie z dzielników w zakresie do danej liczby powyżej------------------')

#Zad 3
def znajdź_liczby_doskonałe_zad3(zakres):
    lista_doskonałych=[]
    for cyfry in range(6,zakres+1):
        if cyfry%2==0:                  #lub range to (6,zakres+1,2) wtedy nie daje if cyfry
            if czy_doskonała(cyfry)==True:
                lista_doskonałych.append(cyfry)
        else:
            continue
    return lista_doskonałych
print(znajdź_liczby_doskonałe_zad3(1000))   #orgyinalnie 10000

print('--------Zadanie z znajdywanialiczb doskonałych w zakresiepowyżej----------')
