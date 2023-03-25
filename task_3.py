#свариться коли лямбда не вгорі(чому?)щоб написати програму користувався прикладами з інету
from functools import reduce
arr = [100, 2121, 352, 234242, 1214, 1]
max_element = reduce(lambda a, b: a if a > b else b, arr)
print(max_element)


def find_max(arr):
    max_element = arr[0]
    for elem in arr:
        if elem > max_element:
            max_element = elem
    return max_element


max_element = max(arr)
print(max_element)

max_element = find_max(arr)
print(max_element)






