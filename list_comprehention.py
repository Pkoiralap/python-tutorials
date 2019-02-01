lst = [
    {
        'name': 'Nished',
        'occupation': 'Doctor',
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
        'occupation': 'Engineer',
        'number': 11231412412,
        'salary': 600000,
    }
]

def getItemName(obj):
    if obj['occupation'] == 'Engineer':
        return 'Er. ' + obj['name']
    else:
        return obj['name']

engineers = [
    getItemName(obj)
    for obj in lst
]
print(engineers)