x,y,z = [int(input()) for i in range(3)]

h = x/60 + y/3600
z = z/1.6

print(f"Speed = {z/h:.1f}")
