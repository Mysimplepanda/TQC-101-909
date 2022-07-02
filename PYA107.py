input_number=[str(input()) for i in range(5)]
interger_number=list(map(float, input_number))
print(" ".join(input_number))




print(f"Sum = {sum(interger_number):.1f}")
print(f"Average = {sum(interger_number)/len(interger_number):.1f}")
