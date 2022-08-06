#selection sort
#Quadratic runtime O(n^2)
#In selection sort we find the minimum and place it at the beginning of array
#Then we sequentially find other minimums and place them one after another creating sorted list


#polish version:
#sortowanie przez wybieranie
#kwadratowa złożoność czasowa

def sortowanie_przez_wybieranie(tablica):

    for i in range(0,len(tablica)-1):
        minIndex=i
        for j in range(i+1,len(tablica)):
            if tablica[minIndex]>tablica[j]:
                minIndex=j

        '''pom=tablica[minIndex]
        tablica[minIndex]=tablica[i]
        tablica[i]=pom'''

        tablica[i],tablica[minIndex]=tablica[minIndex],tablica[i]
    return tablica
print(sortowanie_przez_wybieranie([5,8,3,2,7,9,1,4]))

print('--------------------')


