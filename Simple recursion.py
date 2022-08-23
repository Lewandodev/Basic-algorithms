#ALGORYTMY REKURENCYJNE
#RECURSIVE ALGORITHMS

#Recursion example
#przykład rekurencji
def rekur(n):
    if n%2==0:
        if n ==2:
            return 2
        else:
            return rekur(n-1)+n
    else:
        return rekur(n-1)
print(rekur(11))

print('--------------------')
#Zad 1
def suma_nieparzystych(n):
    if n%2!=0:
        if n==1:
            return 1
        else:
            return suma_nieparzystych(n-1)+n
    else:
        return suma_nieparzystych(n-1)
print('Suma liczb nieparzystych do 100',suma_nieparzystych(100))

#Zad 2
#suma pięciu liczb rekruencyjnie
def sumapieciu(limit,liczba):
    if limit==5:
        return liczba
    return sumapieciu(limit+1,liczba*liczba)+liczba
print('\nSuma pięciu liczb:',sumapieciu(1,2))


#Rekurencja średniozaawansowane przypadki
#silnia jest jednym z najprostszych przykładów rekurencji

def zwroc_silnie(n):
    if n==1 or n==0:
        return 1
    else:
        return n*zwroc_silnie(n-1)
print(zwroc_silnie(6))
print('--------------------')

#algorytm fibonacciego można rozwiązać z użyciem metod rekurencyjnych bądź iteracyjnych
#rekurencja w algorytmach fibonacciego jest jednak nieefektowna czasowo i musi zostać poddana memoizacji
def fibonacii(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonacii(n-1)+fibonacii(n-2)
print(fibonacii(6))

#innym przykładem rekurencji jest algorytm ekulidesa

def NWD_rekurencyjne(a,b):
    if b!=0:
        return NWD_rekurencyjne(b,a%b)
    return a