#Merge sort (polish version and commentary will be added later)

#Merge sort uses Divide and conquer algorithm in order to work
#Divide and conquer algorithm works by breaking down problem (list/array) in multiple subprolblems (sublists) recursively
#until they become simple to solve and are combined to solve original problem
#the created sublists will already one element arrays which we will be merging together to make them sorted

#Merge sort has O(n*log(n)) time complexity

list_to_sort=[9,5,3,1,6,8,7,4,2]

def merge_sort(array):
    if len(array)>1:
        left_array=array[0:len(array)//2]
        right_array=array[len(array)//2:]
    else:
        return array

    #recurisve merging
    merge_sort(left_array)
    merge_sort(right_array)


    #merge of left most and rigt most elements
    i=0 #left most element in left array
    j=0 #left most element in right array

    k=0 #merged array index

    while i<len(left_array) and j<len(right_array):
        if left_array[i]<right_array[j]:
            array[k]=left_array[i]
            i+=1
        else:
            array[k]=right_array[j]
            j+=1

        k+=1

    while i<len(left_array): #every elemen. of right array are in sorted but we miss elmn. from left array
        array[k]=left_array[i]
        i+=1
        k+=1

    while j<len(right_array): #every elemen. of left array are in sorted but we miss elmn. from right array
        array[k]=right_array[j]
        j+=1
        k+=1

    return array



print('unsorted array:',list_to_sort)
print('sorted array:',merge_sort(list_to_sort))