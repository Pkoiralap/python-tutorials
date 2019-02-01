a = {}
def change_a(val):
    a = val
    print('inside func', a)

def change_a_mutate(val):
    a['key'] = val
    print('inside func', a)


change_a(5)
print('outside func', a)
print()

change_a_mutate(10)
print('outside func', a)