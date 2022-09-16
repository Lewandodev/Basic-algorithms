#Algorytm zachłanny
#Greedy algorithm

#A greedy algorithm is any algorithm that follows the problem-solving heuristic of making the locally optimal choice at each stage
#Algorytm zachłanny  – algorytm, który w celu wyznaczenia rozwiązania w każdym kroku dokonuje zachłannego, tj. najlepiej rokującego w danym momencie wyboru rozwiązania


#Greedy algorithm returning the change from multiple coins
#for example: 7 can be returned in 2 coins

def ile_monet(reszta):
    monety=[1,2,5]
    liczba_moent_do_wydania=0

    while reszta>0:
        nominal_do_wydania=0
        for nominal in monety:
            if(nominal<=reszta
                 and nominal>nominal_do_wydania):
                nominal_do_wydania=nominal
        reszta-=nominal_do_wydania
        liczba_moent_do_wydania+=1

    return liczba_moent_do_wydania

print('z ilu monet wydać możemy 7',ile_monet(7))



#exercise

def transoprt_mąki(ilość_mąki):
    pojeność_opakowań=[15,5,2,1]
    liczba_opakowań=0

    while ilość_mąki>0:
        odejmowana_masa=0
        for opakowania in pojeność_opakowań:
            if opakowania<=ilość_mąki and opakowania>odejmowana_masa:
                odejmowana_masa=opakowania

        ilość_mąki-=odejmowana_masa
        liczba_opakowań+=1
    return liczba_opakowań

print(transoprt_mąki(68))
