# TODO
setx=set({})
sety=set({})

print("Enter group X's subjects:")
# TODO
sub=input()
while sub !="end":
    setx.add(sub)
    sub=input()

print("Enter group Y's subjects:")
# TODO
sub=input()
while sub !="end":
    sety.add(sub)
    sub=input()


ans=setx.union(sety)
print(sorted(ans))


ans=setx.intersection(sety)
print(sorted(ans))


ans=sety.difference(setx)
print(sorted(ans))


ans=setx.symmetric_difference(sety)
print(sorted(ans))


