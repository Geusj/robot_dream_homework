import time


def func_name_and_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.asctime()
        result = func(*args, **kwargs)
        with open("task2.txt",  "a", encoding="utf-8") as f:
            f.write(f"Функція {func.__name__} була викликана. Час виконання: {start_time}.\n")
            f.write(f"Результат виконання: {result}\n")
        return result

    return wrapper


@func_name_and_time
def my_function_1(x, y, z):
    return (x * y) / z


result = my_function_1(834234, 12, 1231)
print(result)
