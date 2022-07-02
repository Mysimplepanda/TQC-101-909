print("Input to set1:")

seta=set([input() for i in range(5)])

print("Input to set2:")

setb=set([input() for i in range(3)])

print("Input to set3:")

setc=set([input() for i in range(9)])




print(f"set2 is subset of set1: {setb.issubset(seta)}")
print(f"set3 is superset of set1: {setc.issuperset(seta)}")


