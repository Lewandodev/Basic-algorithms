#selection sort
#Quadratic runtime O(n^2)
#In selection sort we find the minimum and place it at the beginning of array/list
#Then we sequentially find next minimums other than the already existing ones and place them in order

new_array=[1,9,11,2,7,3,8,4,5,10,6]

def selection_sort(array):
    #we need 2 loops the outer loops which goes from left to right and finds the "first" minimums to order
    for i in range(0,len(array)-1): #we can skip last element since we will have nothing to compare the last elmn. with
        min_index=i  #the current index of our minimum number
        #next we need inner loop which checks if there is a element smaller than current minimum
        #the inner loops starts at index: i
        for j in range(i+1,len(array)):
            if array[j]<array[min_index]:
                min_index=j
        #after inner loop is finished the min_index will be the smallest element right to i
        #(smallest number in all unordered numbers)

        array[i],array[min_index]=array[min_index],array[i]
        #the swap of i elmn. with min_index  and vice versa
    return array

print('unordered:',new_array)
print('ordered:',selection_sort(new_array))


#polish version:
#sortowanie przez wybieranie
#kwadratowa złożoność czasowa
#podczas sorotwania przez wybieranie będziemy szukali najmniejszej wartości i ustawiali ją na początku
#Potem szukamy innych minimów i ustawiamy je na "początku" za posortowanymi elementami listy


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


