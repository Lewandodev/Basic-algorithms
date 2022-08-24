#Bisection method
#Metoda połowienia

#Bisection method is used for finding a root of a continuous function in numerical interval
#Metoda Połowienia Przedziałów służy do znajdowania miejsca zerowego pewnej ciągłej funkcji f ograniczonej do pewnego przedziału

#dla funkcji f=x+2
#for f=x+2 math function



#our continuous function is defined as following: y=ax+b with epsilon being precision value
#funkcja liniowa/ciągła jest definiowana jako: y=ax+b, epsilon odpowiada za skalę dokładności wyznaczonego miejsca zerowego

def wartosć_funkcji(x):
    return x+2
    #in this function we declare Value of function
    #w tej funkcji deklarujemy naszą funkcję liniową

def połowienie_przedziałów(a,b,epsilon):
    if wartosć_funkcji(a)==0:
        return a
    if wartosć_funkcji(b)==0:
        return b
    #if either a or b equals 0 our root is already found as it is a or b
    #w przypadku gdy a lub b wynosi 0 nasze miejsce zerowe jest jedną z tych zmiennych

    while b-a>epsilon:
        środek=(a+b)/2
        if wartosć_funkcji(środek)==0:
            return środek
        if wartosć_funkcji(a)*wartosć_funkcji(środek)<0:
            środek=b
        else:
            a=środek
    return (a+b)/2


#ZADANIA PONIŻEJ
#Exercises


import math



#ZADANIE 1
#EXERCISE 1

def w_FUNKCJA(x):
    return x**2-4*x-6

def Z1połowienie(a,b,epsilon):
    if w_FUNKCJA(a)==0:
        return a
    if w_FUNKCJA(b)==0:
        return b

    while b-a>epsilon:
        środek=(a+b)/2
        if w_FUNKCJA(a)*w_FUNKCJA(środek)<0:
            b=środek
        else:
            a=środek
    return (a+b)/2
print('Zadanie 1: ')
print(round(Z1połowienie(0,20,0.001),4))

#ZADANIE 2
#EXERCISE 2

def w2_funkcji(x):
    return 2*(x**3)+2

def Z2_połowienie(a,b,epsilon):
    if w2_funkcji(a)==0:
        return a
    if w2_funkcji(b)==0:
        return b

    while b-a>epsilon:
        środek=(a+b)/2
        if w2_funkcji(środek)==0:
            return środek
        if w2_funkcji(a)*wartosć_funkcji(środek)<0:
            b=środek
        else:
            a=środek
    return (a+b)/2

print('Zadanie 2:')
print(round(Z2_połowienie(0,1,0.001),3))
