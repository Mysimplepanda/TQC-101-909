def compute(x):
    pri=0
    if x <= 1:
        pri=1
    
    for i in range(2,x):
        if x % i == 0:
            pri=1
            break
    if pri == 0:
        print("Prime")
    else:
        print("Not Prime")
compute(int(input()))
