import time


def func_name_and_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.asctime()
        result = func(*args, **kwargs)

        print(f"Функція {func.__name__} була викликана. Час виконання: {start_time} .")
        return result

    return wrapper


@func_name_and_time
def my_function_1(x, y, z):
    return (x * y) / z


result = my_function_1(834234, 12, 1231)
print(result)


@func_name_and_time
def data(set_1, set_2):
    return set1.symmetric_difference(set2)


set1 = {"Lviv", "Ternopil", "Franuk", 1, 2, 3, 4, 5}
set2 = {"New York", "Lviv", 3, 4, 5, 6, 7}
print(data(set1, set2))