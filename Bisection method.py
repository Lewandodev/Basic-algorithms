#marked for recision after I come from vacation 

#dla funkcji f=x+2

def wartosć_funkcji(x):
    return x+2

def połowienie_przedziałów(a,b,epsilon):
    if wartosć_funkcji(a)==0:
        return a
    if wartosć_funkcji(b)==0:
        return b

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








import math









#ZADANIE 1
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
