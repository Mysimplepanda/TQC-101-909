numbers=[int(input()) for i in range(10)]
times=0

for i in numbers:
    if numbers.count(i) > times:
        this_num=i
        times=numbers.count(i)
print(this_num)
print(times)
