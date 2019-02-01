def generator():
    try:
        a = 5
        print('going first')
        yield a
        print('going 2nd')
        a = 9
        yield a
        print('going third')
        a = 7
        yield a
        return 'all good'
try:
    iterator = generator()
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    a = 'a' + 5
except Exception as err:
    print('err', err)
