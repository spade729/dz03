"""Exercise 02.

Даны два списка, в списках допустимы повторяющимися элементы, необходимо поменять их
значения между собой без использования других списков и картежей.
"""

arr1 = [ 1, 2, 3, 4, 5]
arr2 = ['q', 'w', 'v', 'n', 'u', '5g', 'qwe', 'jkkkk']

print('До:')
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

#arr1, arr2 = arr2, arr1
#arr1[0:len(arr1)], arr2[0:len(arr2)] = arr2[0:len(arr2)], arr1[0:len(arr1)]
arr1[:], arr2[:] = arr2[:], arr1[:]

print('После:')
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))