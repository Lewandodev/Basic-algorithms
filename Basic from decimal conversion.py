#basic conversion from decimal to systems up to 9

def decimal_upTo9_conv(cipher,system):
    inverted='' #this variable stores inverted rest divisions of user inserted cipher
    n=cipher
    while n!=0:
        r=n//system
        c=n%system
        c=str(c)  #we need to convert the value to string to avoid errors
        inverted=c+inverted
        n=r
    return inverted

print('Converting values up to 9 conversion of 166 to 4 system:',decimal_upTo9_conv(166,4))
print('Converting values up to 9 conversion of 38 to 3 system:',decimal_upTo9_conv(38,3))
def decymalny_na_binarny(cyfra):
    odwr='' # ta zmienna przechowuje czytane od tyłu reszty z dzielenia wprowadzonej przez uzytkowniaka cyfyr przez 2
    sys=2 #bo binarny dzielimy przez 2 w innych systemach może być 4 3 8 itd
    n=cyfra
    while n!=0:
        r=n//sys
        c=n%sys
        c=str(c)  #konwertujemy na stringa wartość żeby nie wywalało błedów
        odwr=c+odwr
        n=r
    return odwr

print('\nzamiana 20 na system binarny',decymalny_na_binarny(20))

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

print('\n15 zamiana z sys. dec. na system 9:',decymalny_do_9(15,9))

print('\n17 zamiana z sys. dec. na system 6:',decymalny_do_9(17,6))









#additional note: as I'm now back from vacation I decided to start revising some of the algorithm projects that I was unable to edit during my holidays
#the extensions of all the files will be changed from .txt to .py with additional new code and commentary