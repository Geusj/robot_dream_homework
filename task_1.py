phone_book = {}

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
    elif command == "delete":
        if name and name in phone_book:
            del phone_book[name]
    elif command == "stats":
        stats = f"Number of entries: {len(phone_book.keys())}"
        print(stats)
    elif command == "list":
        names = list(phone_book.keys())
        print(names)
    elif command == "show":
        if name and name in phone_book:
            print(f"Name: {name}, Phone: {phone_book[name]}")
