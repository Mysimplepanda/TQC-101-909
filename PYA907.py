filename = input()

with open(filename,"r",encoding="utf-8") as hfile:
    data = hfile.readlines()

print(f"{len(data)} line(s)")

words=0

for line in data:
    wordlist = line.split() #抓出一行文字，並且以空白切開。單字存到 wordlidt
    words += len(wordlist)
    
print(f"{words} word(s)")

chars=0

for line in data:
    wordlist=line.split() #去掉空白，只留下單字
    
    for word in wordlist:
        chars += len(word)

print(f"{chars} character(s)")
