#多個串列的時候，用 index() 來去做多個串列的對應(關聯性)

names = []
heights = []
weights = []

with open("read.txt","r",encoding="utf-8") as hfile:
    
    for line in hfile:
        
        print(line)
        
        data=line.split(" ")
        
        names.append(data[0].strip())
        heights.append(eval(data[1].strip()))
        weights.append(eval(data[2].strip()))

print(f"Average height: {sum(heights) / len(heights):.2f}")
print(f"Average weight: {sum(weights) / len(weights):.2f}")

tallest = max(heights)
tallest_index = heights.index(tallest)
print(f"The tallest is {names[tallest_index]} with {tallest:.2f}cm")

heaviest = max(weights)
heaviest_index = weights.index(heaviest)
print(f"The heaviest is {names[heaviest_index]} with {heaviest:.2f}kg")
