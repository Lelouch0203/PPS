# def ContainsDupli(arr):
#     m=[]
#     for i in arr:
#         if i in m:
#             return True
#         else:
#             m.append(i)
#     return False
# arr=[1,2,3,3]
# print(ContainsDupli(arr))
def ContainsDupli(arr):
    return len(arr) != len(set(arr))

arr = [1, 2, 3, 3]
print(ContainsDupli(arr))
    