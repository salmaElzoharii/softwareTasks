#insertionSort
arr=[8,100,40,2,1,0,6,7,6]
for i in range(1,len(arr)):
    nOfPasses=i
    comparator=i-1
    turn=i
    while(nOfPasses ):
        if(arr[turn]<arr[comparator]):
            arr[turn],arr[comparator]=arr[comparator],arr[turn]
            nOfPasses-=1
            turn=comparator
            comparator-=1
        else:
            break
print("Array after sorting: ",arr)