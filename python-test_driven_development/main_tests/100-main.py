#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
print(matrix_mul([[3, 1, 4]], [[4, 3], [2, 5], [6, 8]]))
m_a = [[1, 2, 3], [3, 4, 5]]
m_b = [[1, 2], [3, 4]]
print(matrix_mul(m_a, m_b))