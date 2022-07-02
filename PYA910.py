f_name="read.dat"

with open(f_name,"r",encoding="utf-8") as hfile:
    
    datalist = hfile.readlines()

print(datalist[0])

male=0
female=0

for i in range(1, len(datalist)):
    print(datalist[i])
    
    data = datalist[i].split(" ")
    
    if data[2] == "0":
        female += 1
    else:
        male += 1
    
print(f"Number of males: {male}")
print(f"Number of females: {female}")
