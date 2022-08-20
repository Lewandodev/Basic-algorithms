#Rekurencyjne wyznaczanie wartości ciągu fibonacciego

def fibonacii(n):
    if n==1:
        return 1
    if n==0:
        return 0
    #w przypadku liczb 1 bądź 0 zwracamy 0 lub 1
    #trzy pierwsze liczby w ciągu fibonacciego (licząc od 0) to 0,1,1
    if n!=1 or 0:
        return fibonacii(n-1)+fibonacii(n-2) #każde kolejene liczby to suma liczb poprzedniej i poprzedzającej poprzednią
        #tym samym żeby otrzymać np wartość 4 będziemy cofać się rekurencyjnie aż do base casea (którym jest 1 i 0)
        #i zliczać po kolei otrzymane 'odpowiedzi' na kolejne cyfry w ciągu

for i in range(0,10):
    print(i,'liczba w ciągu fibonacciego to:',fibonacii(i))

print("\n16 liczba ciągu fibonacciego:",fibonacii(16))


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
