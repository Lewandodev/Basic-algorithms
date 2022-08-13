#Algorithm will be revised once I'm back from vacation
print('------Zadania z Euklidesa Iteracyjnie------')
print('---Zad 1 ponizej------')
#Zad 1
def NWDeuklides(a,b):
    pom=0
    while b!=0:
        pom=b
        b=a%b
        a=pom
    return a
print(NWDeuklides(15,20))
print(NWDeuklides(250,1025))
print(NWDeuklides(13,917))


print('--------Zad 2 ponizej------')
#Zad 2
def znajdź_nwd_wielu_liczb(lista_liczb):
    for i in range(0,len(lista_liczb)):
        return NWDeuklides(NWDeuklides(lista_liczb[i],lista_liczb[i+1]),lista_liczb[len(lista_liczb)-1])

print(znajdź_nwd_wielu_liczb([6, 12, 30]))
print(znajdź_nwd_wielu_liczb([12, 36, 78, 120]))
print(znajdź_nwd_wielu_liczb([244, 1024, 4024, 5096, 10020, 17448]))
