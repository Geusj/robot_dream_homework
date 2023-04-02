def data(set_1, set_2):
    return set1.intersection(set2)


set1 = {"Lviv", "Ternopil", "Franuk", 1, 2, 3, 4, 5}
set2 = {"New York", "Lviv", 3, 4, 5, 6, 7}
print(list(data(set1, set2)))

