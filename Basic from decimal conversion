def decymalny_na_binarny(cyfra):
    odwr='' # ta zmienna przechowuje czytane od tyłu reszty z dzielenia wprowadzonej przez uzytkowniaka cyfyr przez 2
    sys=2 #bo binarny dzielimy przez 2 w innych systemach może być 4 3 8 itd
    n=cyfra
    while n!=0:
        r=n//sys
        c=n%sys
        c=str(c)  #konwertujemy na steringa wartość żeby nei wywaliło błedu
        odwr=c+odwr
        n=r
    return odwr

print(decymalny_na_binarny(20))

def decymalny_do_9(cyfra,sys):
    odwr='' # ta zmienna przechowuje czytane od tyłu reszty z dzielenia wprowadzonej przez uzytkowniaka cyfyr przez 2
     #do 9 system może być dowolny od 2 do 9 bez 10 bo wtedy muszą byc wartości ascii
    n=cyfra
    while n!=0:
        r=n//sys
        c=n%sys
        c=str(c)  #konwertujemy na steringa wartość żeby nei wywaliło błedu
        odwr=c+odwr
        n=r
    return odwr

print(decymalny_do_9(15,9))

print(decymalny_do_9(17,6))
