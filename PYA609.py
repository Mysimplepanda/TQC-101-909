#TODO


print("Enter matrix 1:")
#TODO

mat1=[]
for i in range(2):
    tmp=[]
    for j in range(2):
        
        #置於迴圈內，依給定之格式輸出
        print("[%d, %d]: " % (i+1, j+1), end = '')
        num=int(input())
        tmp.append(num)
    mat1.append(tmp)



print("Enter matrix 2:")
#TODO
mat2=[]
        #置於迴圈內，依給定之格式輸出
for i in range(2):
    tmp=[]
    for j in range(2):
        
        #置於迴圈內，依給定之格式輸出
        print("[%d, %d]: " % (i+1, j+1), end = '')
        num=int(input())
        tmp.append(num)
    mat2.append(tmp)





print("Matrix 1:")
#TODO
for row in mat1:
    for i in row:
        print(f"{i} ",end="")
    print()
print("Matrix 2:")
#TODO
for row in mat2:
    for i in row:
        print(f"{i} ",end="")
    print()
print("Sum of 2 matrices:")
#TODO
for i in range(2):
    for j in range(2):
        sum_num=mat1[i][j]+mat2[i][j]
        print(f"{sum_num} ",end="")
    print()
