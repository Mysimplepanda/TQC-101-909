num=int(input())
sec=0
for i in range(num):
    sec+=1
    output=[f"{j:<2}* {sec:<2}= {sec*j:<4}" for j in range(1,num+1)]
    print("".join(output))
