rows=int(input())
cols=int(input())

def compute(mylist):
    for i in mylist:
        print(f"{i:4}",end="")#不斷行也不空格
    print()
    
    
for i in range(rows):
    mylist=[]
    for j in range(cols):
        mylist.append(j-i)
    compute(mylist)
