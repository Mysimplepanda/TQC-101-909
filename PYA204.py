def compute(x,y,z):
    if z == "+":
        return x+y

    if z == "-":
        return x-y
    
    if z == "*":
        return x*y
    
    if z == "/":
        return x/y
        
    if z == "//":
        return x//y

    if z == "%":
        return x%y
print(compute(int(input()),int(input()),input()))
