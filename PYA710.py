mydict={}

key=input("Key: ")
while key !="end":
    value=input("Value: ")
    mydict[key]=value
    key=input("Key: ")

see=input("Search key: ")
print(see in mydict)


