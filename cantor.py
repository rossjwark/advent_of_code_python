import numpy as np

def triangle(r, c):
    return ((r + c + 1)**2 - (r + c + 1)) / 2.

def diagonal(r, c):
    return c

def compute_cantor_index(row, col):
    return triangle(row, col) + diagonal(row, col)


def get_code_val(row, col):
    cantor_index = compute_cantor_index(row-1, col-1)

    value = 20151125
    for i in range(int(cantor_index)):
        value = value * 252533 % 33554393

    print(value)


def _cantor_test():
    square_dim = 5
    
    arr = np.zeros((square_dim, square_dim))
    

    for i in range(square_dim):
        for j  in range(square_dim):
            arr[i, j] = triangle(i, j) + diagonal(i, j)

    print(arr)


if __name__ == "__main__":
    get_code_val(1, 1)
    get_code_val(2, 1)
    get_code_val(6, 6)
    get_code_val(2978, 3083)
