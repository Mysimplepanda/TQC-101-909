key=input()
cap=0
alp=0
num=0
leng=0

if len(key) >=8:
    leng+=1
for i in key:
    if i in "qwertyuiopasdfghjklzxcvbnm":
        alp=1
    if i in "QWERTYUIOPASDFGHJKLXCVBNM":
        cap=1
    if i in "0123456789":
        num=1
if sum([cap,alp,num,leng])==4:
    print("Valid password")
else:
    print("Invalid password")
