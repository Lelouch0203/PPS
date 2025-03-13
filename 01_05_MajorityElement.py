def majority(arr):
    count=0
    num= None
    for i in arr:
        if count==0:
            num=i
        if i==num:
            count+=1

        else:
            count-=1
       
    return num

arr=[2,2,1,1,1,2,2,1,1]
print(majority(arr))
            
        
    