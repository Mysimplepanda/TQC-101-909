def compute(x,y):
    print(max([i for i in range(1,min([x,y])+1) if x % i == 0 and y % i == 0]))

[x,y]=list(map(int, input().split(",")))
compute(x,y)
