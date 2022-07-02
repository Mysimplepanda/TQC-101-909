def print_off(bmi):

    if bmi < 18.5:
        state="under weight"
    elif bmi < 25:
        state="normal"
    elif bmi < 30:
        state="over weight"
    else:
        state="fat"

    print(f"BMI: {bmi:.2f}")
    print(f"State: {state}")

m=float(input())/100
while m != -99.99:
    kg=float(input())
    print_off(kg/m**2)
    m=float(input())/100



