#не працює як треба
a = input("Enter text:")
match a:
    case int():
        print("ціле число")
    case float():
        print("число з плаваючою комою")


