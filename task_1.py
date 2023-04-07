def recursion(n):
    if n == -1:
        return n
    print(n)
    return recursion(n-1)


user_number = input(f"Write your number:")
recursion(int(user_number))
