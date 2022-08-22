# Prime Factorization algorithm
# Algorytm rozkładu liczby na czynniki pierwsze
print('---Rozkład liczby na czynniki pierwsze---')
print('\nrozkład na czynniki różnych liczb ')


# algorytm w wersji bazowej


def rozloz_na_czynniki(n):
    koniec = 'wypisano wszystkie dzielniki'  # wiadomość po wypisaniu wszystkich dzielników
    i = 2  # najmniejszy możliwy dzielnik to 2 jeżeli n nie dzieli się przez 2 nasze i(dzielnik) będzie zwiększane
    while n > 1 and i * i <= n:  # albo i<=(n**0.5) rozkład wyjonujemy dopóki n jest większe niż 1 oraz kwadrat dzielnika jest nie większy niż dzielona liczba
        # w ten sposób zapobiegamy sytuacjom w których n próbowalibyśmy podzielić przez za dużą liczbę i zoptymalizujemy czas działania alg.
        while n % i == 0:
            print(i)
            n = n / i  # podczas rozkładu n musi być redukowane o dzielnik podczas iteracji w celu znalezienia pozostałych
        i += 1
    if n > 1:
        # w przypadku gdy nie znajdziemy żadnego i mogącęgo być dzielnikiem
        # naszym finalnym dzielnikiem może być sama liczba (n)
        print(int(n))
        return koniec
    elif n == 1:
        # dojście n do 1 oznacza wypisanie wszystkich dzielników, zwracamy zmienną "koniec" aby uniknąć zwrotu "none"
        return koniec


print('\nRozkład na czynniki 36')
print(rozloz_na_czynniki(36))
print('\nRozkład na czynniki 1512')
print(rozloz_na_czynniki(1512))
print('\nRozkład na czynniki 17')
print(rozloz_na_czynniki(17))

print('\nZmodyfikowany rozkład na czynniki')


# Zadanie z rozkładu na czynniki

def rozloz_na_czynniki_modifykowany(n):
    lista = []
    i = 2
    while n > 1 and i * i <= n:
        while n % i == 0:
            if i not in lista:
                lista.append(i)
            n = n / i
        i += 1
    if n > 1:
        if n not in lista:
            lista.append(int(n))
    return lista


# zmodyfikowany algorytm bazuje na uprzedniej funkcji rozkładowej z tą różnicą, że szuka on jedynie unikalnych dzielników
# w celu pozyskania unikalnych dzielników możemy użyć listy z odpowiednią funkcją bądź setu który przechowuje unikalne wartości

print('\nUnikalne dzielniki 36:')
print(rozloz_na_czynniki_modifykowany(36))
print('\nUnikalne dzielniki 1512:')
print(rozloz_na_czynniki_modifykowany(1512))
print('\nUnikalne dzielniki 17:')
print(rozloz_na_czynniki_modifykowany(17))


def factorize(n):
    i = 2  # smallest possible divisor
    endstat = 'Those are all divisors'

    while n > 1 and i <= (
            n ** 0.5):  # we will be iterating and dividing till n is greater than 1 and square of our current divisor isn't greater than n
        while n % i == 0:  # this will prevent our algorithm from using too big numbers and optimze running time
            print(i)
            n = n / i  # in order to get all the divisors while factorizing we need to reduce our number by the current divisor
        i += 1

    if n > 1:  # if we run out of optimal i divisors our final divisor will be the number itself
        print(int(n))
        return endstat
    if n == 1:  # if n is reduced to 1 our algorithm is already finished we return "endstat" in order to prevent returning "none" value
        return endstat


print('\nPrime factorization of 40:')
print(factorize(40))

print('\nPrime factorization of 19:')
print(factorize(19))

print('\nModified prime factorization')


# Zadanie z rozkładu na czynniki

def modified_prime_fact(n):
    setuniq=set()

    i = 2
    while n > 1 and i <= int(n ** 0.5):
        while n % i == 0:

            setuniq.add(i)
            n = n / i
        i += 1

    if n > 1:
        setuniq.add(n)

    return setuniq

#modified factorization will be returning only unique divisors of the number
#otherwise it's the same as the standard function

print('\nUnique divisors of 28:')
print(modified_prime_fact(28))


print('\nUnique divisors of 52:')
print(modified_prime_fact(52))


#Algorithm revised