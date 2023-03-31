phone_book = {}

while True:

    name = input("Enter name:")
    if name == "End":
        break
    second_name = input("Enter second name:")
    phone_number = input("Enter phone number:")
    birthday = input("Enter date of birth:")

    phone_book[name] = {"second name:": second_name, "phone number:": phone_number,
                        "date of birth:": birthday}

# add new customer

add = phone_book["Vova"] = "+3801"

# delete any customer

del phone_book["Vova"]

# calculation customers

stats = f"Number of entries: {len(phone_book.keys())}"
print(stats)

# list of oll customers(Names)

list = dict.keys(phone_book)
print(list)

# information by name
# working when you entered name "Andrii"
show = print(phone_book["Andrii"])
