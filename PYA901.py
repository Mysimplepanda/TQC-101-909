hfile = open("write.txt","w",encoding="utf-8")

[hfile.write(input()+"\n") for i in range(5)]

hfile.close()
