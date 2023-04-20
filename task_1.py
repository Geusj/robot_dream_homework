import json
phone_book = {}
file = open("phone_book.json", "a+")
json_str = json.dumps(phone_book)

while True:
    user_data = input("Enter data(use command :add,delete,stats,show,list):")
    if user_data == "last":
        break

    data = user_data.split()
    command = data[0]
    name = data[1] if len(data) > 1 else None

    if command == "add":
        phone = data[2]
        if name and name not in phone_book:
            phone_book[name] = phone
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
    file.write(user_data + "\n")
file.close()

file = open("phone_book.json", "r")
for line in file:
    print(line)
file.close()
