def count(x):
    if x % 4 == 0 and x % 9 == 0:
        return x
    elif x % 4 == 0:
        return x
    elif x % 9 == 0:
        return x
    else:
        return "delete"
    
banum=list(map(count,list(range(int(input()),int(input())+1))))
while "delete" in banum:
    banum.remove("delete")

full_line=len(banum)//10
unfull_numbers=len(banum)%10
times=0

for i in range(full_line):
    for j in range(0,10,1):
        print(f"{banum[j+i*10]:<4}",end="")
    print("\n",end="")
    times+=1
for i in range(unfull_numbers):
    print(f"{banum[i+times*10]:<4}",end="")
print("\n",end="")

print(len(banum))
print(sum(banum))
    








