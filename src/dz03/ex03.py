"""Exercise 03.

Создать программу, которая умеет перемножать матрицы. Можно ограничиться матрицами
не более чем 3x3.
Матрицу 3x3 вполне можно записать так: matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
"""

def check_is_matrix(matrix:list)->bool:
    """check_is_matrix.

    Args:
        matrix (list): _description_

    Returns:
        bool: _description_
    """
    first = 0

    for i in matrix:       
       if first == 0:
           m_str_len = len(i)   
           first = -1
       
       if m_str_len != len(i):
           return False
    
    return True

def check_multiplication_posible(matrix1:list, matrix2:list)->bool:
    """check_multiplication_posible.

    Args:
        matrix1 (list): _description_
        matrix2 (list): _description_

    Returns:
        bool: _description_
    """
    return len(matrix1[0]) == len(matrix2)

def fm_multiplication(matrix1:list, matrix2:list)->list:
    """FM.

    Args:
        matrix1 (list): _description_
        matrix2 (list): _description_

    Returns:
        list: _description_
    """
    if not check_is_matrix(matrix1):
        print('матрица 1 - не матрица')
        return None

    if not check_is_matrix(matrix2):
        print('матрица 2 - не матрица')
        return None
    
    if not check_multiplication_posible(matrix1,matrix2):
        print('кол-во столбцов матрицы 1 отличается от кол-ва строк матрицы 2')
        return None
    
    lines   = len(matrix1)
    columns = len(matrix2[0])
    m_num   = len(matrix2)
 
    result = []

    for i in range(lines):
        result.insert(i,[])        
        
        for j in range(columns):   
           result[i].insert(j,0)
           for m in range(m_num):
                result[i][j] += matrix1[i][m] * matrix2[m][j]
    
    return result


m1 = [[1, 2, 3], 
      [4, 5, 6]]

m2 = [[ 7,  8,  9, 10],
      [11, 12, 13, 14],
      [15, 16, 17, 18]]

m3 = fm_multiplication(m1,m2)

if m3 is not None:
    for line in m3:
        print(line)

m1 = [[1, 2, 3, 4], 
      [4, 5, 6]]

m2 = [[ 7,  8,  9, 10],
      [11, 12, 13, 14],
      [15, 16, 17, 18]]

m3 = fm_multiplication(m1,m2)

if m3 is not None:
    for line in m3:
        print(line)


m1 = [[1, 2, 3, 4], 
      [4, 5, 6, 7]]

m2 = [[ 7,  8,  9, 10],
      [11, 12, 13, 14],
      [15, 16, 17, 18]]

m3 = fm_multiplication(m1,m2)

if m3 is not None:
    for line in m3:
        print(line)