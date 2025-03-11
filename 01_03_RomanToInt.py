romans={
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
    
}
def romanToInt(str):
    ans=0
    for i in range(len(str)):
        if i<len(str)-1 and romans[str[i]]<romans[str[i+1]]:
            ans-=romans[str[i]]
        else:
            ans+=romans[str[i]]
    return ans

print(romanToInt('XLV'))
