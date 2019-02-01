lst = [
    {
        'name': 'Nished',
        'occupation': 'Engineer',
        'number': 123123,
        'salary': 500000,
    },
    {
        'name': 'Suyog',
        'occupation': 'Engineer',
        'number': 1123143123,
        'salary': 400000,
    },
    {
        'name': 'Kedar',
        'occupation': 'Footballer',
        'number': 11231412412,
        'salary': 600000,
    }
]

def filter_func(item):
    return item['occupation'] == 'Engineer'

def map_numbers(item):
    return item['number']

engineers = list(filter(filter_func, lst))
numbers = list(map(map_numbers, engineers))