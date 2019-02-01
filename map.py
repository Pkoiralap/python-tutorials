items = ['Ram', 'Shyam', 'Hari']

def custom_map(func, lst):
    result = []
    for item in lst:
        mapped_result = func(item)
        result.append(mapped_result)
    return result

def mapFunc(item):
    return item*2

mapped_items = custom_map(mapFunc, [1,2,3,4,5])

print(mapped_items)