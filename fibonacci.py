fib_cache = {}


def fibonacci(n):
    value = 0
    if n in fib_cache:
        return fib_cache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n - 1) + fibonacci(n - 2)

    fib_cache[n] = value

    return value


# for i in range(1, 11):
#     print(i, ':', fibonacci(i))

def fibonacci_1(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        first_value = 1
        second_value = 1
        for i in range(3, n + 1):
            result = first_value + second_value
            first_value = second_value
            second_value = result
        return result


# for i in range(1, 11):
#     print(i, ':', fibonacci_1(i))

def fib_2(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b
    return a


for i in range(1, 11):
    print(i, ':', fib_2(i))
