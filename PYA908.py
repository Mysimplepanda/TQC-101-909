#單字 : 出現次數
#dict {單字:出現次數}  key:單字 value:出現次數
#list : two list [紀錄單字]-[出現次數]
#tuple(x) : 需掃描單字，更改出現次數

f_name = input()
n = int(input())
mydict={}

with open(f_name,"r",encoding="utf-8") as hfile:
    data=hfile.read() #string

words=data.split()
for w in words: #抓出每一單字
    w.strip()
    if w not in mydict.keys():
        mydict[w] = 1
    else:
        mydict[w]+=1

mylist=[]
for mykey in mydict.keys():
    if mydict[mykey]==n:
        mylist.append(mykey)

mylist.sort()
for i in mylist:
    print(i)
