#Bubble sort algorithm

#bubble sort is the most popular and one of the easiest sorting types

A=[6,3,5,1,2,8,9,11,256,0,22,77,32591,124040,29,40]

def bubble_sort(lista):
    for i in range(0,len(lista)-1):
        for j in range(0,len(lista)-i-1):
            if lista[j]>lista[j+1]:
                pom=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=pom

    return lista

print(bubble_sort(A))


#More information about bubble sort algorithm:
#function checks if the next element is lower than the current one, if it is the element from array is moved
#since we check if the next (+1) element is lower than the current one we need to reduce length of array by one
