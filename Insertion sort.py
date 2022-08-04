#insertion sort






#insertion sort polish version:
#wersja sortowania przez wstawianie po polsku

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