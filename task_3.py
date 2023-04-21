import time


def func_name_and_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.asctime()
        result = func(*args, **kwargs)
        with open("task3.txt", "a", encoding="utf-8") as f:
            f.write(f"Функція {func.__name__} була викликана. Час виконання: {start_time}.\n")
            f.write(f"Результат виконання: {result}\n")
        return result

    return wrapper


@func_name_and_time
def my_function_1(x, y):
    return x * y


try:
    start_time = time.asctime()
    result = my_function_1(int(12, 2))
except Exception as e:
    print(f"Помилка: {e}")
    with open("task3.txt", "a", encoding="utf-8") as f:
        f.write(f"Помилка: {e} виникла о {start_time}.\n")
