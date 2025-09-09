
import numpy as np

def matrix_addition(matrix1, matrix2):
    """
    두 개의 행렬을 더하는 함수
    :param matrix1: 첫 번째 행렬 (numpy 배열)
    :param matrix2: 두 번째 행렬 (numpy 배열)
    :return: 두 행렬의 합 (numpy 배열)
    """
    c_np = matrix1 + matrix2    # numpy를 사용한 행렬의 덧셈 연산
    return c_np






# Numpy 배열（행렬）생성 （3x3 행렬）
a_np = np.array ([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

b_np = np.array ([
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
])

matrix_np = matrix_addition(a_np, b_np)

print(matrix_np)