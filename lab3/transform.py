import numpy as nm

functions = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
             [1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1],
             [1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1],
             [1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1],
             [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]]


def int_to_bin(n):
    s = str(bin(n))
    b = [0] * 5
    i = 2
    for c in s[::-1]:
        if c == 'b':
            break
        elif int(c) == 1:
            b[i] = 1
        i -= 1

    return b


def get_wal_funcs():
    wal = [None] * 32
    for i in range(32):
        n = int_to_bin(i)
        r_c = [n[4] ^ n[3], n[3] ^ n[2], n[2] ^ n[1], n[1] ^ n[0], n[0] ^ 0]

        wal[i] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        for j in range(5):
            if r_c[j] != 0:
                for k in range(32):
                    wal[i][k] *= functions[j][k]

    return wal


def get_matrix(coef):

    def create_current_matrix(matrix):
        l = len(matrix)
        result = nm.empty([l * 2, l * 2], dtype=int)

        for r in range(l):
            for c in range(l):
                result[r][c] = result[r + l][c] = result[r][c + l] = matrix[r][c]
                result[r + l][c + l] = - matrix[r][c]

        return result

    if coef == 0:
        return [[1]]
    else:
        prev_matr = get_matrix(coef - 1)
        return create_current_matrix(prev_matr)


def fut(signal):
    def fun(a):
        l = len(a)
        if l == 1:
            return a
        else:
            up = fun(a[0:int(l / 2)])
            down = fun(a[int(l / 2):l])
            return list(map(lambda x, y: x + y, up, down)) + list(map(lambda x, y: x - y, up, down))

    return list(map(lambda x: x / 32, fun(signal)))


def ifut(signal):
    def fun(a):
        l = len(a)
        if l == 1:
            return a
        else:
            up = fun(a[0:int(l / 2)])
            down = fun(a[int(l / 2):l])
            return list(map(lambda x, y: x + y, up, down)) + list(map(lambda x, y: x - y, up, down))

    return fun(signal)


def dut(signal):
    return list(map(lambda x: x / 32, get_matrix(5).__matmul__(nm.array(signal).transpose())))


def idut(signal):
    return get_matrix(5).transpose().__matmul__(nm.array(signal).transpose())