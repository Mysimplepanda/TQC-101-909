f_name = input()
str_old = input()
str_new = input()

with open(f_name, "r", encoding="utf-8") as hfile:
    data = hfile.read()

print("=== Before the replacement")
print(data)

new_data = data.replace(str_old, str_new)
print("=== After the replacement")
print(new_data)
