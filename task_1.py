# зробив 2 прирівняння бо свариться(пропонує перейменувати)
argument = input("Enter argument:")
power_of_argument = input("Enter power of argument:")
a = argument
b = power_of_argument


def check_function(argumen, power_of_argumen):
    a = int(argumen)
    b = int(power_of_argumen)
    result = a ** b
    print(result)
    return argument


check_function(a, b)
