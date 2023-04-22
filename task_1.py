import json

try:
    with open("phone_book.json", "r") as phonebook_f:
        records = phonebook_f.read()
        phone_book = json.loads(records)
except FileNotFoundError:
    phone_book = {}

while True:
    user_data = input("Enter data(use command :add,delete,stats,show,list):")
    if user_data == "last":
        with open("phone_book.json", "w") as phonebook_f:
            json.dump(phone_book, phonebook_f)
        break

    data = user_data.split()
    command = data[0]
    name = data[1] if len(data) > 1 else None

    if command == "add":
        phone = data[2]
        if name and name not in phone_book:
            try:
                phone_book[name] = int(phone)
            except ValueError:
                print("The phone number can only contain numbers")
    elif command == "delete":
        if name in phone_book:
            del phone_book[name]
        else:
            print("This user is not in the phone book")

    elif command == "stats":
        stats = f"Number of entries: {len(phone_book.keys())}"
        print(stats)
    elif command == "list":
        names = list(phone_book.keys())
        print(names)
    elif command == "show":
        if name in phone_book:
            print(f"Name: {name}, Phone: {phone_book[name]}")
        else:
            print("This user is not in the phone book")
    elif command != "show" and command != "list" and command != "stats" and command != "delete" and command != "add":
        print("This command not exist")


