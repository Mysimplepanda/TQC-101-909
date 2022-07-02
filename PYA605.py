numbers=[int(input()) for i in range(10)]
numbers.remove(max(numbers))
numbers.remove(min(numbers))
print(sum(numbers))
print(f"{sum(numbers)/8:.2f}")
