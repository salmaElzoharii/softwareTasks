def binarySearchRec(arr,key,low,high):

    mid=low+((high-low)//2)
    if(high>=low):
        if(key==arr[mid]):
            return mid
        if(key>arr[mid]):
            return binarySearchRec(arr,key,mid+1,high)
        elif(key<arr[mid]):
            return binarySearchRec(arr, key, low, mid-1)
flag=1
numbers = []
size = int(input("Enter number of elements : "))
print("enter the list: ")
for i in range(0, size):
    numbers.append(int(input()))
element=int(input("Enter the number: "))
numbers.append(element)
numbers.sort()
indexofElement=binarySearchRec(numbers,element,0,len(numbers)-1)
left=0
right=indexofElement-1
while(right>left):
    if(numbers[left]+numbers[right]==element):
        print("yes,",element," = ",numbers[left],"+",numbers[right])
        flag=0
        break
    elif(numbers[left]+numbers[right]<element):
        left+=1
    elif(numbers[left]+numbers[right]>element):
        right-=1

if(flag==1):
    print("no")


