#Basic euclidean algorithm
#Algorytm Euklidesa

#Algorytm Euklidesa – algorytm wyznaczania największego wspólnego dzielnika dwóch liczb.
#w algorytmach będziemy modyfikowali głównie wartości wyjściowe 2 wprowadzonych liczb do czasu aż jedna z nich wyniesie 0


print('Iteracyjna wersja algorytmu Euklidesa')
print('Największe dzielniki:')

#Iteracyjna wersja algorytmu Euklidesa jest nieco trudniejsza od rekurencyjnej ale działa na tej samej zasadzie
def NWDeuklides(a,b):
    pom=0   #zmienna pomocnicza potrzebna nam będzie aby zapisać "przetworzone" zmienne inaczej algorytmu nie przyjąłby poprzedniej wartości b
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
    '''for i in range(0,len(lista_liczb)):
        return NWDeuklides(NWDeuklides(lista_liczb[i],lista_liczb[i+1]),lista_liczb[len(lista_liczb)-1])'''

    while len(lista_liczb) > 2:
        a= NWDeuklides(lista_liczb[len(lista_liczb) - 2], lista_liczb[len(lista_liczb) - 1])
        lista_liczb.pop()
        lista_liczb.pop()
        lista_liczb.append(a)
    if len(lista_liczb)==2:
        return NWDeuklides(lista_liczb[0], lista_liczb[1])



print(znajdź_nwd_wielu_liczb([6, 12, 30]))
print(znajdź_nwd_wielu_liczb([12, 36, 78, 120]))
print(znajdź_nwd_wielu_liczb([244, 1024, 4024, 5096, 10020, 17448]))



#rekurencyjna wersja algorytmu Ekuklidesa
#najprostszą wersją algorytmu ekulidesa jest ta w której używamy rekurencji algorytm jest niezwykle krótki i dobrze czytelny

print('\nAlgorytm Ekuklidesa wersja rekurencyjna')
print('Największe dzielniki liczb:')


def NWD_rekurencyjne(a,b):
    if b!=0:  #rekurencja będzie trwała dopóki reszta z dzielenia b (lub a) nie będzie równa 0
        return NWD_rekurencyjne(b,a%b) #dzięki zastosowaniu rekurencji nie potrzebujemy zmiennej pomocniczej
    return a

print('\nnajwiększegy wspólny dzielnik 15 oraz 20',NWD_rekurencyjne(15,20))
print('największegy wspólny dzielnik 200 oraz 1025',NWD_rekurencyjne(200,1025))
print('największegy wspólny dzielnik 17 oraz 913',NWD_rekurencyjne(17,913))



#second revision