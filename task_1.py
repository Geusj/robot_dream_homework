#мені здається я не зовсім зозумів завдання
phone_book = {"Andrii": "+38054551", "Vitalii": "+380144", "Natalia": "+380145", "Victor": "+38015474",
              "Nelia": "+38065651", "Julian": "+38014452"}
stats = f"Number of entries: {len(phone_book.items())}"
print(stats)
phone_book["Anna"] = "+380995566"
del phone_book["Anna"]
print(list(phone_book))
for name, number in phone_book.items():
    print(f"{name}: {number}")
all_info = phone_book.get("Andrii")
print(all_info)
