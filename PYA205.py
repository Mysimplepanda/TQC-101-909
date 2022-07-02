text=input()
if text.isalpha():
    print(f"{text} is an alphabet.")
elif text.isdigit():
    print(f"{text} is a number.")
else:
    print(f"{text} is a symbol.")
