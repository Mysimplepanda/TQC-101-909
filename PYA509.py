def compute(ans):
    now=1
    while now < ans[0]+1:
        now+=1
        if ans[0] % now==0 and ans[1] % now == 0:
            ans[0]//=now
            ans[1]//=now
            now=1
    return ans
    


fir=list(map(int, input().split(",")))
sec=list(map(int, input().split(",")))
ans=[fir[0]*sec[1]+sec[0]*fir[1],fir[1]*sec[1]]
ans=compute(ans)




print(f"{fir[0]}/{fir[1]} + {sec[0]}/{sec[1]} = {ans[0]}/{ans[1]}")



