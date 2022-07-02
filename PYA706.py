times=int(input())
for i in range(times):
    string=list(input().lower())
    alphe=list("qwertyuiopasdfghjklzxcvbnm")
    for j in string:
        if j in alphe:
            alphe.remove(j)
    print(alphe==[])
