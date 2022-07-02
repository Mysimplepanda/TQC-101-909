def compute(a,b,c):
    q=b**2-4*a*c

    if q > 0:
        q1=(-b+q**0.5)/(2*a)
        q2=(-b-q**0.5)/(2*a)
        return f"{q1}, {q2}"
    else:
        return "Your equation has no root."


a,b,c = [int(input()) for i in range(3)]

print(compute(a,b,c))
