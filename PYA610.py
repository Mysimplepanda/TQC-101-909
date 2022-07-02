#TODO
every_week=[]

for week in range(1,5):
    print(f"Week {week}:")

    for i in range(1,4):
        every_week.append(eval(input(f"Day {i}:")))
        

print(f"Average: {sum(every_week)/len(every_week):.2f}")
print(f"Highest: {max(every_week)}")
print(f"Lowest: {min(every_week)}")
"""
Week _:
Day _: 
Average: _
Highest: _
Lowest: _
"""
