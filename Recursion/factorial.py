def factorial(n):
    if n == 0:
        return 1
    elif n > 0:
        return n * factorial(n - 1)


print(factorial(5))
print(factorial(0))
print(factorial(1))
print(factorial(-1))
