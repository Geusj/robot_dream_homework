import re
filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print(content)
    new_text = re.sub(r"\b\w+@\w+\.\w+\b", "@", content)
    print(new_text)
except FileNotFoundError:
    print(f"File {filename} not found")
