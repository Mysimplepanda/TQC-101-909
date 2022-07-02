# TODO
times=int(input())

for i in range(times):
    numbers=list(map(float,input().split()))
    print(f"{max(numbers)-min(numbers):.2f}")
