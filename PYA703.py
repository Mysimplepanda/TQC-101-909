text=[]
ask=input()
while ask != "end":
    text.append(ask)
    ask=input()

print(tuple(text))
print(tuple(text[:3:]))
print(tuple(text[-3::]))
