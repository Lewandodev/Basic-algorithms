#Marked by me for recision once I'm back from vacation
print('---Rozkład liczby na czynniki pierwsze---')
print('-------zadanie 1 ponizej---------')
#Zad 1
def rozloz_na_czynniki(n):
    i=2
    while n>1 and i*i<=n:     #albo i<=(n**0.5)
        while n%i==0:
            print(i)
            n=n/i
        i+=1
    if n>1:
         print(int(n))

print(rozloz_na_czynniki(36))
print(rozloz_na_czynniki(1512))
print(rozloz_na_czynniki(17))

print('----------zadanie 2 ponizej-------')
#Zad 2

def rozloz_na_czynniki_modifykowany(n):
    lista=[]
    i=2
    while n>1 and i*i<=n:
        while n%i==0:
            if i not in lista:
                lista.append(i)
            n=n/i
        i+=1
    if n>1:
        if n not in lista:
            lista.append(int(n))
    return lista

print(rozloz_na_czynniki_modifykowany(36))
print(rozloz_na_czynniki_modifykowany(1512))
print(rozloz_na_czynniki_modifykowany(17))
