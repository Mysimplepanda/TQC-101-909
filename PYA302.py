start=int(input())
end=int(input())
print(sum([i for i in range(start+start%2,end+1,2)]))
