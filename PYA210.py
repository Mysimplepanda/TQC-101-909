numbers=sorted([int(input()) for i in range(3)])

print(sum(numbers)) if numbers[0]+numbers[1]>numbers[2] else print("Invalid")

