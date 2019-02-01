from functools import reduce

lst = [
    {
        "name": 'Nished',
        "occupation": "Engineer",
        "number": 123124,
        "salary": 15241212
    },
    {
        "name": 'Sugoy',
        "occupation": "Engineer",
        "number": 123124,
        "salary": 15241212
    },
    {
        "name": 'Kedar',
        "occupation": "Footballer",
        "number": 123124,
        "salary": 15241212
    },
    {
        "name": 'Prasanna',
        "occupation": "Doctor",
        "number": 123124,
        "salary": 15241212
    }
]
#{
#  'Engineer': ['Nished', 'Suyog'],
#  'Footballer': 'Kedar',
#  'Doctor': 'Prasanna'
# }

def reduce_func(acc,item):
    occp = item['occupation']
    if acc.get(occp):
        acc[occp] = [acc[occp] , item['name']]
    else:
        acc[occp] = item['name']
    return acc

distinct_occupations = reduce(reduce_func, lst, {})
print(distinct_occupations)