# 1 1 2 3 5 8 13 ....
known_values = {
    1: 1,
    2: 1
}

def fibonacci(n):
    global known_values
    if n - 1 in known_values.keys():
        n_minus_1_value = known_values.get(n-1)
    else:
        n_minus_1_value = fibonacci(n-1)
        known_values[n-1] = n_minus_1_value

    if n - 2 in known_values.keys():
        n_minus_2_value = known_values.get(n-2)
    else:
        n_minus_2_value = fibonacci(n-2)
        known_values[n - 2] = n_minus_2_value

    return n_minus_1_value + n_minus_2_value

fib_8 = fibonacci(800)
print(fib_8)