def fibonacci(n):
    a = 1
    if n > 2:
        a = fibonacci(n - 1) + fibonacci(n - 2)
    return a


user_number = input(f"Enter you number: ")
number = fibonacci(int(user_number))
print(number)
