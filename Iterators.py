from sys import getsizeof
a = [1,2,3,4]*1000
print(getsizeof(a))

a_iter = iter(a)
print(getsizeof(a_iter))
