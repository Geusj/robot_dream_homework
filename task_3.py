def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


user_number = input(f"Enter you number: ")
number = factorial(int(user_number))
print(number)
