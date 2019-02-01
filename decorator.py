def add4(func):
    def retFunc(a):
        return func(a+4)
    return retFunc

@add4
def multiply_by_two(a):
    return a*2

print(multiply_by_two(3))