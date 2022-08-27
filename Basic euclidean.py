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
        return NWDeuklides(NWDeuklides(lista_liczb[i],lista_liczb[i+1]),lista_liczb[len(lista_liczb)-1]) <---incorrect on long range'''

    while len(lista_liczb) > 2:
        a= NWDeuklides(lista_liczb[0], lista_liczb[1])
        lista_liczb.remove(lista_liczb[0])
        lista_liczb.remove(lista_liczb[1])
        lista_liczb.insert(0,a)
    if len(lista_liczb)==2:
        return NWDeuklides(lista_liczb[0], lista_liczb[1])


print('NWD liczb [6, 12, 30]:')
print(znajdź_nwd_wielu_liczb([6, 12, 30]))
print('\nNWD liczb [12, 36, 78, 120]:')
print(znajdź_nwd_wielu_liczb([12, 36, 78, 120]))
print('\nNWD liczb [244, 1024, 4024, 5096, 10020, 17448]:')
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



#euclidean algorithm iterative version

def iterative_eculid(a,b):
    aux =0
    while b!=0:
        #in order to find greatest common divisor of 2 numbers we will need to divde one of the numbers by the other
        aux=b
        b=a%b #the divison of numbers will exist as long as there is a remainder
        a=aux  #auxiliary variable is used in order to store the original value of b without it a would have the same value as b
    return a

#iterative version of euclidean algorithm is a bit harder than recursive one in implementation because of the need for the auxiliary variable
#if we forget about it our function won't work properly

print('\neuclidean algorithm iterative version')
print('\nGreatest common divisor of 15 and 20: ',iterative_eculid(15,20))
print('Greatest common divisor of 25 and 225: ',iterative_eculid(25,225))
print('Greatest common divisor of 13 and 177: ',iterative_eculid(13,177))



print('\neuclidean algorithm recursive version ')
#euclidean algorithm recursive version
#recursive version of the euclidean algorithm function is the easiest one to implement and remember

def recursive_euc(a,b):
    if b!=0:  #function works on the same principles as the iterative one as long as remainder isn't 0 function will be calling itself
        return recursive_euc(b,a%b) #because of recursion we don't need any auxiliary variable as a could be referred as b without any complications
    return a

print('\nGreatest common divisor of 1984 and 2020: ',recursive_euc(1984,2020))
print('Greatest common divisor of 12 and 1234: ',recursive_euc(12,1234))
print('Greatest common divisor of 22 and 781: ',recursive_euc(22,781))


#there is actually built in fucntion in python math library that works exactly as the euclidean algorithm and help us find the greatest common divisor
#the math.gcd() function

print('\nFinding GCD of many numbers')

def many_gcd(numblist):

    while len(numblist) > 2:
        a= iterative_eculid(numblist[0], numblist[1])
        numblist.remove(numblist[0])
        numblist.remove(numblist[1])
        numblist.insert(0,a)
    if len(numblist)==2:
        return NWDeuklides(numblist[0], numblist[1])

numberslist=[12, 36, 78, 120]
print('GCD of numbers:',numberslist)
print(many_gcd(numberslist))


#third revision fixed the many gcd algorithm