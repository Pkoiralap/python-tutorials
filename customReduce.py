def custom_reduce(*args):
    'this is a custom reduce function'
    '''
        args[0] : reduce func
        args[1] : items
        args[2] : initial value -> not required'
    '''
    reduce_func = args[0]
    items = args[1]

    if len(items) == 0:
        return 'empty array'
    acc = args[2] if len(args) == 3 else items[0]
    index = 0 if len(args) == 3 else 1

    while index < len(items):
        acc = reduce_func(acc, items[index])
        index += 1
    return acc

value = custom_reduce(lambda acc,item: acc+item, [1,2,3,4,5])
print(value)