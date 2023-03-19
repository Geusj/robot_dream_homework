#entered text "number" or "word"
a = input("Enter text:")
if a.isdigit():
    if a.isdigit() % 2 == 0:
        print("its a number is even")
    else:
        print("its a number odd")
if a.isalpha():
    print(f"its a text whose length is {len(a)}")


