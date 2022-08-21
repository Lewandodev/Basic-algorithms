print('Sprawdzanie czy liczba jest doskonała ')
#Sprawdzanie czy liczba jest doskonała
#liczba doskonała to taka liczba naturalna, która jest równa sumie wszystkich swoich podzielników, mniejszych od tej liczby.

def czy_doskonała(n):
    suma_dzielników=0
    dzielniki=[]
    for i in range(1,(n//2)+1):
        #podczas sprawdzania dzielników możemy pominąć cyfry większe od połowy naszej liczby gdyż nigdy nie będą one naszymi dzielnikami
        if n%i==0:
            dzielniki.append(i)

    for cyfyr_dzielników in dzielniki:
        suma_dzielników+=cyfyr_dzielników
    #otrzymane dzielniki dodajemy w ceku zweryfikowania czy ich suma dałaby nam liczbę doskonałą
    if suma_dzielników==n:
        return True
    else:
        return False

print('czy 8128 jest liczbą doskonałą?:',czy_doskonała(8128))

print('\nZadanie z sprawdzania lcizb doskonałych w zakresie:')


def znajdź_liczby_doskonałe(zakres):
    lista_doskonałych=[]

    for cyfry in range(1,zakres+1):
        if czy_doskonała(cyfry)==True:
            lista_doskonałych.append(cyfry)
            #jeżeli dana cyfra jest doskonała dodajemy ją do naszej listy
    return lista_doskonałych

print('liczby doskonałe w zakresie do 100:',znajdź_liczby_doskonałe(100))

print('\nZadanie z znajdywania liczb doskonałych w zakresie zoptymalizowane')


def znajdź_liczby_doskonałe_zad3(zakres):
    lista_doskonałych=[]
    for cyfry in range(6,zakres+1): #lub range to (6,zakres+1,2) wtedy nie sprawdzamy czy dzieli się bez reszty przez 2
        if cyfry%2==0:     #w optymalizacji pomijamy wszystkie nieparzyste cyfry w zakresie
            if czy_doskonała(cyfry)==True:
                lista_doskonałych.append(cyfry)
        else:
            continue
    return lista_doskonałych
print('liczby doskonałe w zakresie do 10000:',znajdź_liczby_doskonałe_zad3(10000))

print('\nChecking if number is perfect')



#checking if the number is perfect
#perfect number is a positive integer that is equal to the sum of its proper divisors


def is_perfect(n):
    divisors_sum=0
    divisors=[]
    for i in range(1,(n//2)+1):
        #while looking for divisors we can skip all the numbers that are bigger than our number divided by 2 they will never be divisors
        if n%i==0:
            divisors.append(i)

    for cyfyr_dzielników in divisors:
        divisors_sum+=cyfyr_dzielników
    #otrzymane dzielniki dodajemy w ceku zweryfikowania czy ich suma dałaby nam liczbę doskonałą
    if divisors_sum==n:
        return True
    else:
        return False

print('Is 8128 perfect?:',czy_doskonała(8128))

print('\nExercise searching for perfect numbers in range:')


def find_perfect_numbs(rangee):
    list_perfect=[]

    for numbs in range(1,rangee+1):
        if is_perfect(numbs)==True:
            list_perfect.append(numbs)
    return list_perfect

print('perfect numbers in range from 1 to 100:',find_perfect_numbs(100))

print('\nExercise searching for perfect numbers in range optimized')


def find_perfnumbs_opt(rangee):
    list_of_perfs=[]
    for numbs in range(6,rangee+1): #or we use range(6,range+1,2) with step (2) in order to don't use the if function
        if numbs%2==0:    #in optimized version we skip all the odd numbers fastening up our running time
            if is_perfect(numbs)==True:
                list_of_perfs.append(numbs)
        else:
            continue
    return list_of_perfs
print('perfect numbers in range up to 10000:',find_perfnumbs_opt(10000))


#algorithm revised
