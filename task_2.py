def sum_args(*numbers):
    print(f"args: {numbers}")
    result = sum(numbers)
    print(f"sum: {result}")
    return result

sum_args(1, 2, 3, 4, 5)

