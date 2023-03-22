text = input("Enter text:")
for i in text:
    if i.isdigit():
        if int(i) % 2 == 0:
            print(f"number {i} even")
        else:
            print(f"number {i} odd")
    elif i.isalpha():
        if i.isupper():
            print(f"capital {i} letter")
        else:
            print(f"small {i} leter")
    else:
        print(f" {i} symbol")


