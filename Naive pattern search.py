#wyszukiwanie wzorca
#głównym celem jest wyszukiwanie czy np. jakiś ciąg znaków występuje w naszym zdaniu albo słowie
#Sprawdzanie będzie polegało na zweryfikowaniu czy w danym wyrażeniu możliwe jest znalezienie szukanego wzorca.
#szukamy najpierw pierwszej litery ze wzorca w wyrażeniu, a następnie sprawdzamy czy kolejne znaki pokrywają się także ze wzorcem
#dodatkowo sprawdzamy czy szukany wzorzec zmieści się w wyrażeniu

def czy_wzorzec(wyr,wzorz):
    pierWzorz=wzorz[0]

    for i in range(0,len(wyr)):
        if pierWzorz==wyr[i] and len(wyr)-i-len(wzorz)>=0:  #sprawdzamy czy szukany wzorzec zmieści się w wyrażeniu
            wzór=True
            for j in range(1,len(wzorz)):
                if wzorz[j]!=wyr[i+j]:
                    wzór=False
            if wzór==True:
                return True

    return False

print(czy_wzorzec('ala ma kota','ta'))
print(czy_wzorzec('adam je ryz','je ryzy'))
print(czy_wzorzec('kota dał','a d'))

print('zadanie 1 ponizej: ')
#ZADANIE 1
def cyfr_czy_wzorzec(wry,wzor):
    wry=str(wry)
    wzor=str(wzor)
    pierWzor=wzor[0]

    for i in range(0,len(wry)):
        if pierWzor==wry[i] and len(wry)-i-len(wzor)>=0:
            stały_wzorzec=True
            for j in range(1,len(wzor)):
                if wzor[j]!=wry[i+j]:
                    stały_wzorzec=False

            if stały_wzorzec==True:
                return True
    return False

print(cyfr_czy_wzorzec(291952,95))
print(cyfr_czy_wzorzec(93200125,21))