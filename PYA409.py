vote1=0
vote2=0
trash_vote=0

for i in range(5):
    your_vote=input()
    if your_vote == "1":
        vote1+=1
    elif your_vote == "2":
        vote2 += 1
    else:
        trash_vote +=1
    
    
    print(f"Total votes of No.1: Nami =  {vote1}")
    print(f"Total votes of No.2: Chopper =  {vote2}")
    print(f"Total null votes =  {trash_vote}")

if vote1 > vote2:
    print(f"=> No.1 Nami won the election.")
if vote2 > vote1:
    print(f"=> No.2 Chopper won the election.")
if vote1 == vote2:
    print(f"=> No one won the election.")


