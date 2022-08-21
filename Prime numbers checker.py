#liczby pierwsze
#liczba pierwsza to taka która dzieli się jedynie przez jeden i samą siebie



#najprostsza wersja algorytmu
def funkcja_czy_pierwsza(n):
    if n<=1:
        return False #sprawdzamy tylko dodatnie liczby + jeden nie jest liczbą pierwszą
    else:
        for i in range(2,n): #będziemy przechodzili przez wszystkie cyfry od 2 do do liczby poprzedzającą sprawdzaną (nie bierzemy pod uwagę n)
            if n%i==0:     #w celu wykluczenia potencjalnych dzielników innych niż 1 oraz nasza liczba
                return False #jeżeli znajdziemy inny dzielnik wiemy że liczba nie jest pierwsza
        return True

print('Czy 17 to liczba pierwsza?:',funkcja_czy_pierwsza(17))
print('\nBardziej wydajna wersja algorytmu 1:')
#powyższa wersja lagorytmu jest jednak mało wydajna w przypadku liczba składających się z wielu cyfr
#np.:dla liczby 81948157 algorytm będzie przechodził aż do cyfry 81948156 zabierając zbyt dużo czasu

#Bardziej wydajne wersje algorytmu:
#pierwsza wersja
def wydajana_funkcja_czy_pierwsza1(n):

    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1): #idziemy tylko do pierwiastka z n bo sqr(n)*sqr(n) to nadal n
        if n%i==0:                #pierwiastek z n jest swoistą "granicą" dzielników sprawdzanej liczby
            return False #aby lepiej zoobrazować rozłóżmy 16: 1*16,2*8,4*4(nasz pierwiastek z n),8*2,16*1 liczby za pierwiastkiem to to samo w innej kolejności
    return True                  #dla liczby która nie jest kwadratowa np: 18 pierwiastkową granicą byłby pierwiastek z 18 zaokrąglony w dół


print('czy 100000 jest liczbą pierwszą?:',wydajana_funkcja_czy_pierwsza1(100000))


print('Bardziej wydajna wersja algorytmu 2:')

#druga wersja
def wydajana_funkcja_czy_pierwsza2(n):
    if n<=1:
        return False
    if n==2:
        return True   #w drugiej wersji dodatkowo sprawdzamy czy wprowadzona liczba nie jest 2
    if n>2 and n%2==0: #oraz czy nie jest ona parzysta
        return False
    for i in range(3,int(n**0.5)+1,2): #sprawdzając dzielniki możemy przejść od 3 i skakać co 2 wykluczając wszystkie liczby parzyste
        if n%i==0:
            return False
    return True

print('czy 81948157 jest liczbą pierwszą?:',wydajana_funkcja_czy_pierwsza2(81948157))

print('\nzadanie z szukania w zakresie')

#Zadanie
def znajdź_liczby_pierwsze(zakres):
    zakresliczbowy = []
    for liczby in range(1,zakres):
        if wydajana_funkcja_czy_pierwsza1(liczby)==True:
            zakresliczbowy.append(liczby)
    return zakresliczbowy

print('liczby pierwsze w zakresie do 30:')
print(znajdź_liczby_pierwsze(30))


#prime number checker algorithm
#prime number is a number which is divisible only by 1 and self


#most basic version of algorithm:
def is_number_prime(n):
    if n<=1:
        return False #we only check positive numbers and those that are not 1
    else:
        for i in range(2,n): #we will be going through all the numbers from 2 to penultimate number to our number in loop
            if n%i==0:     #we check if our number can be divided by any of the numbers we are looping through
                return False #if so we return false
        return True
#this version of algorithm is inefficient with huge numbers such as 81948157 as we will be checking if any of the numbers from 2 up to 81948156
#can serve as divisor therefore the function will take too much time

print('\nis 17 a prime number?:',is_number_prime(17))


#more efficient version
def efficient_is_number_prime1(n):

    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1): #to test for divisors we only need to test integers up to square root of n
        if n%i==0:            #square of n is the border used to eliminate duplicate products
            return False #to visualize it better lets decompose 16: 1*16,2*8,4*4(our square),8*2,16*1 the factorizations after square of 16 are the same
    return True             #only in reverse order for non perfect square numbers like 18 the border is just sqr(n) but round down

print('more efficient version 1:')

print('is 100000 prime number?:',efficient_is_number_prime1(100000))


print('\nmore efficient version 2:')

#druga wersja
def efficient_is_number_prime2(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n>2 and n%2==0: #we check if the number is not 2 or even since if the number is even it won't be prime
        return False
    for i in range(3,int(n**0.5)+1,2): #while checking for the divisors we can cover only odd numbers this will fasten up the running time of our function
        if n%i==0:
            return False
    return True

print('is 100000 prime number?:',efficient_is_number_prime2(81948157))

print('\nExercise: prime numbers in range')

#Zadanie
def znajdź_liczby_pierwsze(zakres):
    zakresliczbowy = []
    for liczby in range(1,zakres):
        if wydajana_funkcja_czy_pierwsza1(liczby)==True:
            zakresliczbowy.append(liczby)
    return zakresliczbowy

print('prime numbers in the range from 1 to 30:')
print(znajdź_liczby_pierwsze(30))



#Algorithm revised