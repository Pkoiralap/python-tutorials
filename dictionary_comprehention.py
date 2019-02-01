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

people = {
    obj['name']: obj['occupation']
    for obj in lst
}
print(people)