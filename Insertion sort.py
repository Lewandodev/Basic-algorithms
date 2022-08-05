#insertion sort

#we will be dividing our list in the "sorted" and unsorted part every iteration
#we start from one element in "sorted" part and add the others from "unsorted"
#each of the element in "sorted" half of our list is compared with other elements
#the elements from other half (the "unsorted" half) will be added gradually

unsortedlist=[7,2,9,1,3,4,6,5]

def insertion_sort(list):
    for i in range(1,len(list)):
        j= i
        while list[j-1]>list[j] and j>0:
            auxiliary=list[j]
            list[j]=list[j-1]
            list[j-1]=auxiliary
            j-=1
    return list

print(unsortedlist)
print('sorted list: ',insertion_sort(unsortedlist))

#insertion sort polish version:
#wersja sortowania przez wstawianie po polsku

#listę będziemy dzielić na posortowaną i nieposortowaną w każdej iteracji
#listę "posorotwaną" będziemy poszerzali stopniowo dodając elemnty z nieposortowanej części
#każdy elemnt z pierwszej "posortowanej" połowy porównujemy z innymi elementami żeby sprawdzić czy jest na dobrym miejscu

def sortow_przez_wstawianie(list):
    n=len(list)

    for i in range(1,n):
        j=i
        while j>0 and list[j]<list[j-1]:
            pom=list[j]
            list[j]=list[j-1]
            list[j-1]=pom
            j-=1
    return list

print(sortow_przez_wstawianie([5,8,3,2,7,9,1,4]))