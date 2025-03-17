r1=int(input("Enter number of rows in matrix1:"))
c1=int(input("Enter number of columns in matrix1:"))
r2=int(input("Enter number of rows in matrix2:"))
c2=int(input("Enter number of columns in matrix2:"))

if r1 != r2 or c1 != c2:
	print("Matrices dimensions do not match. Cannot add the matrices.")
else:
    m1=[];m2=[]
    print("Enter the elements into the matrix 1:")
    for i in range(r1):
        row=[]
        for j in range(c1):
            row.append(int(input()))
        m1.append(row)
    print(m1)
    for i in range(r2):
        row=[]
        for j in range(c2):
            row.append(int(input()))
        m2.append(row)
    print(m2)
    
    print("Result:")
    result =[]
    
    for i in range(r1):
        row=[]
        for j in range(c1):
            row.append(m1[i][j]+m2[i][j])
        result.append(row)
    print(result)
            
    