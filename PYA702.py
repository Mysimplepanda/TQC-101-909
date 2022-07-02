num=[]
for i in range(1,3):
    print(f"Create tuple{i}:")
    ask=int(input())

    while ask != -9999:
        num.append(ask)
        ask=int(input())
print(f"Combined tuple before sorting: {tuple(num)}")
print(f"Combined list after sorting: {sorted(num)}")


    
