def TwoSum(arr,target):
    m={}
    for i,x in enumerate(arr):
        y=target-x
        if y in m:
            return[m[y],i]
        else:
            m[x]=i
arr=[1,3,4,5]
target= 7
print(TwoSum(arr,target))
