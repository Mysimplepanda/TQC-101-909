num=[]
ask=int(input())
while ask != -9999:
    num.append(ask)
    ask=int(input())


print(tuple(num))

print(f"Length: {len(num)}")
print(f"Max: {max(num)}")
print(f"Min: {min(num)}")
print(f"Sum: {sum(num)}")
