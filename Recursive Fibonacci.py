#Rekurencyjne wyznaczanie wartości ciągu fibonacciego

def fibonacii(n):
    if n==1:
        return 1
    if n==0:
        return 0
    if n!=1 or 0:
        return fibonacii(n-1)+fibonacii(n-2)


print("16 liczba ciągu fibonacciego")
print(fibonacii(16))

print('----------Zadanie z ciągufibonacciego nizej-----')
#Zadanie
'''Napisz funkcję (w formie kodu języka programowania) znajdź_liczby_z_ciągu_fibonacciego, która będzie przyjmować jeden parametr: zakres. 
Następnie zwróci kolejne wartości z ciągu Fibonacciego z zadanego zakresu. Możesz wykorzystać funkcję, która została napisana w ramach poprzedniego zadania.'''

def znajdź_liczby_z_ciągu_fibonacciego(zakres):
    lista=[]
    liczba_obecna=0
    n=0
    while liczba_obecna<zakres:
        liczba_obecna=fibonacii(n)
        if zakres>=liczba_obecna:
            lista.append(fibonacii(n))
        n+=1
    return lista

print(znajdź_liczby_z_ciągu_fibonacciego(50))

#First Revision
