num=int(input())
sec=0
for i in range(num):
    sec+=1
    output=[f"{sec*j:>4}" for j in range(1,sec+1)]
    print("".join(output))
