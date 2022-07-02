times=int(input())
for i in range(times):
    ask=input()
    num=list(map(int, list(ask)))
    print(f"Sum of all digits of {ask} is {sum(num)}")

    
