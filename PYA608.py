list1=[eval(input()) for i in range(9)]

mn=max(list1)
mi=list1.index(mn)

nn=min(list1)
ni=list1.index(nn)


print(f"Index of the largest number {mn} is: ({mi//3}, {mi%3})")
print(f"Index of the smallest number {nn} is: ({ni//3}, {ni%3})")
