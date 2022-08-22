#Basic euclidean
#Algorytm Euklidesa

#Algorytm Euklidesa – algorytm wyznaczania największego wspólnego dzielnika dwóch liczb.

print('Iteracyjna wersja algorytmu Euklidesa')
print('Największe dzielniki:')

#Iteracyjna wersja algorytmu Euklidesa jest nieco trudniejsza od rekurencyjnej ale działa na tej samej zasadzie
def NWDeuklides(a,b):
    pom=0   #zmienna pomocnicza potrzebna nam będzie aby zapisać "przetworzone" zmienne inaczej algorytmu nie zadziałałby poprawnie
    while b!=0:
        pom=b
        b=a%b #b staje się resztą z dzielenia a przez b
        a=pom #a a przyjmuje poprzednią wartość b przed przetworzeniem
    return a

print('\nnajwiększegy wspólny dzielnik 15 oraz 20',NWDeuklides(15,20))
print('największegy wspólny dzielnik 250 oraz 1025',NWDeuklides(250,1025))
print('największegy wspólny dzielnik 13 oraz 917',NWDeuklides(13,917))



print('\nZnajdywanie NWD wielu liczb')
#Zadanie ze znajdywania
def znajdź_nwd_wielu_liczb(lista_liczb):
    for i in range(0,len(lista_liczb)):
        return NWDeuklides(NWDeuklides(lista_liczb[i],lista_liczb[i+1]),lista_liczb[len(lista_liczb)-1])

print(znajdź_nwd_wielu_liczb([6, 12, 30]))
print(znajdź_nwd_wielu_liczb([12, 36, 78, 120]))
print(znajdź_nwd_wielu_liczb([244, 1024, 4024, 5096, 10020, 17448]))



#first revision