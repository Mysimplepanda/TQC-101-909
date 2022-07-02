mydict={}

key=input("Key: ")
while key !="end":
    value=input("Value: ")
    mydict[key]=value
    key=input("Key: ")

keys=sorted(list(mydict.keys()))

[print(f"{i}: {mydict[i]}") for i in keys]


