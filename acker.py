# string="AABCAAADA"
# out=[string[i:i+3] for i in range(0,len(string),3)]

# def unique_characters(s):
#     seen = set()
#     result = []
#     for char in s:
#         if char not in seen:
#             seen.add(char)
#             result.append(char)
#     return ''.join(result)

# for segment in out:
#     print(unique_characters(segment))
n=7
meetings=[[2,4],[1,3]]   
import numpy

meetings=sorted(meetings)
new=numpy.array(meetings).flatten
print(meetings)