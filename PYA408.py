numbers=list(map(lambda x:x%2,[int(input()) for i in range(10)]))

print(f"Even numbers: {numbers.count(0)}")
print(f"Odd numbers: {numbers.count(1)}")
