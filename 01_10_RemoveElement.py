def removeElement(arr,val):
    count=0
    for i in range(0,len(arr)):
        if arr[i]==val:
            count+=1
            arr[i]="-"
    return arr,count
arr=[3,3,2,2,3,1,3]
val=3
print(removeElement(arr,val))