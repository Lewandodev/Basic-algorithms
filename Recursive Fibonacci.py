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
        #i zliczać po kolei otrzymane 'odpowiedzi' na kolejne cyfry w ciągu czyli fibonacii(3)+fibonacii(2) z fibonacci(2) otrzymujemy base casey i wracamy do góry

for i in range(0,10):
    print(i,'liczba w ciągu fibonacciego to:',fibonacii(i))

print("\n16 liczba ciągu fibonacciego:",fibonacii(16))


#english recursive fibonacci algorithm

def fib(n):
    #first we declare base case/cases for our algorithm

    if n==1:
        return 1
    if n==0:
        return 0
    # first 2 values in fibonacci sequence (counting from 0) are 0 and 1 for zero number value and one in the sequence

    if n!=1 or 0:
        return fib(n-1)+fibonacii(n-2)
    #our recursive function will 'descend' till it reaches the base case and 'ascend' with the answers for the next numbers
    #till it reaches the requested number for example: to find the value of number four in fibonacci sequence we first need to find fib(3) and fib(2)
    #from fib(3) we get fib(2) and fib(1) whcih is base case from fib(2) we get 2 base cases as we get answers for the lower fibonacci values
    #we ascend till we reach our requested value

print('\nnumber 16 in fibonacci sequence is:',fib(16))

print('\nFunction which returns fibonacci values for numbers from user range entered by user')
users_range=[1,2,3,4,5,6,7]

def range_to_fiboancii(userrange):
    list=[]

    for i in userrange:
        list.append(fib(i))

    return list
print('Entered range:',users_range)
print('Converted to Fibonacci numbers',range_to_fiboancii(users_range))

print('\n-------Zadanie z ciągu fibonacciego -----')
print('Funkcja podająca wartości liczb w ciągu fibonacciego dla danego zakresu liczb')
#Zadanie
'''Napisz funkcję (w formie kodu języka programowania) znajdź_liczby_z_ciągu_fibonacciego, która będzie przyjmować jeden parametr: zakres. 
Następnie zwróci kolejne wartości z ciągu Fibonacciego z zadanego zakresu. Możesz wykorzystać funkcję, która została napisana w ramach poprzedniego zadania.'''

def znajdź_liczby_z_ciągu_fibonacciego(zakres):
    lista=[]
    for i in zakres:
        lista.append(fibonacii(i))

    return lista
print('Podany zakres:',[1,2,3,4,5,6,7])
print('Liczby z ciągu fibonacciego odpowiadające zkresowi:',znajdź_liczby_z_ciągu_fibonacciego([1,2,3,4,5,6,7]))


#Second Revision
