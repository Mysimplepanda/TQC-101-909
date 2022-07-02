numbers=[int(input()) for i in range(12)]

print(f"{numbers[0]:>3}{numbers[1]:>3}{numbers[2]:>3}")
print(f"{numbers[3]:>3}{numbers[4]:>3}{numbers[5]:>3}")
print(f"{numbers[6]:>3}{numbers[7]:>3}{numbers[8]:>3}")
print(f"{numbers[9]:>3}{numbers[10]:>3}{numbers[11]:>3}")
print(sum(numbers[::2]))
