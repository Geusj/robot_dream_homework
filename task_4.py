text = ["a", 1, 3424, "asd12", 12.2]


def number(x):
    return isinstance(x, (int, float))


number_list = list(filter(number, text))
print(number_list)

number_list = list(filter(lambda x: isinstance(x, (int, float)), text))
print(number_list)
