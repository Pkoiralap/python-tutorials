items = ['Ram', 'Shyam', 'Hari', 'Ram']

def enumerate_custom(lst):
    result = []
    index = 0
    for item in lst:
        pair = (index, item)
        result.append(pair)
        index += 1
    return result

items_to_loop = enumerate_custom(items)
for index,item in items_to_loop:
    print(item, index)