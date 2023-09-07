def binarySearchRec(arr,key,low,high):

    mid=low+((high-low)//2)
    if(high>=low):
        if(key==arr[mid]):
            #print("mid found", mid, " high ", h, " low ", low)
            return 1
        if(key>arr[mid]):
           # print("mid greater",mid," high ",high," low ",low)
            return binarySearchRec(arr,key,mid+1,high)
        elif(key<arr[mid]):
            #print("mid less", mid, " high ", high, " low ", low)
            return binarySearchRec(arr, key, low, mid-1)
    return 0





arr = [1, 5, 7, 10,50,100,600]
flag= binarySearchRec(arr,5, 0, len(arr) - 1)
print(flag)
if (flag == 1):
    print("Element found")
else:
    print("Element not found")