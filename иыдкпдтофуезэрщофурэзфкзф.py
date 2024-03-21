def fibonacci(n):
    if n <= 0:
        return "Ошибка! Введите положительное число."
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Введэите порядковый номер числа Фибоначчи: "))
result = fibonacci(n)
print(f"Число Фибоначчи под номером {n} равно {result}")