arr =[[1,2,2],[2,3,2],[1,2,5]]

def richest(arr):
    newArr=[]
    for i in arr:
        newArr.append(sum(i))
    return max(newArr)
print(richest(arr))
