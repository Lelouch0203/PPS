def redtoZero(n):
    count=0
    while n!=0:
        if n%2==0:
            n/=2
            count+=1
        else:
            n-=1
            count+=1
    return count
print(redtoZero(8))        