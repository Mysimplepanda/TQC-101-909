times=int(input())
for i in range(times):
    fir="*"*(i+1)
    las="*"*i
    space=" "*(times-i-1)
    print(f"{space}{fir}{las}")
    
