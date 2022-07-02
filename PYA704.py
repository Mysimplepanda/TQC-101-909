myset=set({})

ans=int(input())
while ans != -9999:
    myset.add(ans)
    ans=int(input())

print(f"Length: {len(myset)}")
print(f"Max: {max(myset)}")
print(f"Min: {min(myset)}")
print(f"Sum: {sum(myset)}")
