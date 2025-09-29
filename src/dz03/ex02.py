"""Exercise 02.

Даны два списка, в списках допустимы повторяющимися элементы, необходимо поменять их
значения между собой без использования других списков и картежей.
"""

#def fm_swap(arr1: list, arr2: list):
#    """FM."""
    
#    min_arr_len = len(arr1) if len(arr1) < len(arr2) else len(arr2)
    
#    for i in range(min_arr_len):
#        arr1[i], arr2[i] = arr2[i], arr1[i]

    

arr1 = [ 1, 2, 3, 4, 5]
arr2 = ['q', 'w', 'v', 'n', 'u', '5g', 'qwe', 'jkkkk']

print('До:')
print(arr1)
print(arr2)

arr1, arr2 = arr2, arr1

#fm_swap(arr1, arr2)

print('После:')
print(arr1)
print(arr2)