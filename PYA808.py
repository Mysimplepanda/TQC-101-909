SSN=list(map(str, input().split("-")))
if len(SSN[0])==3 and len(SSN[1])==2 and len(SSN[2])==4 and SSN[0].isdigit() and SSN[1].isdigit() and SSN[2].isdigit():
    print("Valid SSN")
else:
    print("Invalid SSN")
