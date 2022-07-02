x1=input()
y1=input()
x2=input()
y2=input()


print(f"( {x1} , {y1} )")
print(f"( {x2} , {y2} )")
[x1,x2,y1,y2]=[float(x1),float(x2),float(y1),float(y2)]
print(f"Distance = {((x1-x2)**2+(y1-y2)**2)**0.5:.4f}")
