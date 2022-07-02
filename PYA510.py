def compute(n):
    if n < 2:
        return n
    else:
        return compute(n-1)+compute(n-2)

num=eval(input())

for i in range(num):
    print(compute(i),end=" ")
    

