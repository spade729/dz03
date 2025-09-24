"""Exercise 01.

Даны два списка, в списках допустимы повторяющимися элементы. Определить входит ли
первый во второй список с учётом количества повторяющихся элементов. Без использования
словарей.
Примеры:
[1, 2, 3, 3, 4]
[1, 2, 3, 7, 4, 3] – входит
[1, 2, 3, 3, 4, 3]
[1, 2, 3, 7, 4, 3] – не входит
[1, 2, 3, 3, 8, 4]
[1, 2, 3, 7, 4, 3] – не входит
[1, 2, 3, “3”, 4]
[1, 2, 3, 7, 4, 3] – не входит
"""

def fm_contain(arr1: list, arr2: list)->bool:
    """FM.

    Args:
        arr1 (list): _description_
        arr2 (list): _description_

    Returns:
        bool: _description_
    """
    arr2_tmp = arr2.copy()

    try:        
        for i in arr1:
            arr2_tmp.remove(i)
    except Exception as e:
        print(e)
        return False
    else:
        return True


 
a1 = [1, 2, 3, 3, 4]
a2 = [1, 2, 3, 7, 4, 3] 

b1 = [1, 2, 3, 3, 4, 3]
b2 = [1, 2, 3, 7, 4, 3]  

c1 = [1, 2, 3, 3, 8, 4]
c2 = [1, 2, 3, 7, 4, 3]  

d1 = [1, 2, 3, '3', 4]
d2 = [1, 2, 3, 7, 4, 3]  

print(fm_contain(a1, a2))
print(fm_contain(b1, b2))
print(fm_contain(c1, c2))
print(fm_contain(d1, d2))
