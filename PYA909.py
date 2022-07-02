f_name = "data.dat"
file = open(f_name,"w",encoding="utf-8")

for i in range(5):
    file.write(input()+"\n")
file.close()

print("The content of \"data.dat\":")

hfile=open(f_name,"r",encoding="utf-8")
for i in hfile:
    print(i)
