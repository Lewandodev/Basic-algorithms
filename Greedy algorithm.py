#Algorytm zachłanny
#Greedy algorithm

#A greedy algorithm is any algorithm that follows the problem-solving heuristic of making the locally optimal choice at each stage
#Algorytm zachłanny  – algorytm, który w celu wyznaczenia rozwiązania w każdym kroku dokonuje zachłannego, tj. najlepiej rokującego w danym momencie wyboru rozwiązania


#Greedy algorithm returning the change from multiple coins
#for example: 7 can be returned in 2 coins

def ile_monet(reszta):
    monety=[1,2,5] #denominations of coins
    liczba_moent_do_wydania=0 #amount of coins we return

    while reszta>0: #while our change is bigger than 0 we will iterate
        nominal_do_wydania=0#current denomination
        for nominal in monety:
            if(nominal<=reszta
                 and nominal>nominal_do_wydania):
                #if denomination is smaller than change and bigger than current denomination we will give in change
                #our current denomination becomes the standard denomiantion
                nominal_do_wydania=nominal
        reszta-=nominal_do_wydania #changes is reduced
        liczba_moent_do_wydania+=1 #amount of coins we will give is increased

    return liczba_moent_do_wydania

print('Z ilu monet wydać możemy 7',ile_monet(7))
print('Amount of coins we can give the change in for 7',ile_monet(7))


#exercise - different type of greedy algorithm
#here we return the amount of packages which we can fill up with flour

def transoprt_mąki(ilość_mąki):
    pojeność_opakowań=[15,5,2,1] #capacity of packages
    liczba_opakowań=0 #the amount of packages we will return

    while ilość_mąki>0: #we iterate as long as the amount of flour is greater than 0
        odejmowana_masa=0 #the substracted flour mass
        for opakowania in pojeność_opakowań: #algorithms go similar to the previous one
            if opakowania<=ilość_mąki and opakowania>odejmowana_masa: #we chceck if the current value of index in packages capacity is less than amount of flour
                #and more than the substracted mass
                odejmowana_masa=opakowania #if so the substracted mass takes the value of package capacity

        ilość_mąki-=odejmowana_masa
        liczba_opakowań+=1
    return liczba_opakowań

print('\nW ilu opakowaniach przetransportujemy 68kg mąki:',transoprt_mąki(68))
print('In how many packages we will transport 68 kilograms of flour:',transoprt_mąki(68))
