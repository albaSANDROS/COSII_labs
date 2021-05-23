import numpy as np
import matplotlib.pyplot as plt

from transform import get_wal_funcs, get_matrix, fut, ifut, dut, idut

N = 32


def _fun(x):
    y = np.cos(2*x) + np.sin(5*x)
    return y


def transformations():
    wal = get_wal_funcs()
    print('Функции Уолша, упорядоченные по частоте')
    for w in wal:

        s = ''
        for i in range(len(w)):
            if w[i] == 1:
                s += '+'
            else:
                s += '-'
        print(s)

    print('Функции Уолша, упорядоченные по Адамару')
    ad_matr = get_matrix(5)
    for m in ad_matr:
        s = ''
        for c in m:
            if c == 1:
                s += '+'
            else:
                s += '-'
        print(s)

    x = np.linspace(0.0, 2 * np.pi, 32)
    function_values = list(map(lambda i: _fun(i), x))

    transform = fut(function_values)
    reverse_transform = ifut(transform)

    first, func = plt.subplots(5, 1, figsize=(5, 8))
    plt.tight_layout()

    func[0].plot(x, function_values)
    func[0].set_title('Исходная функция y=cos(2x)+sin(5x)')
    func[0].grid(True)

    func[1].plot(x, transform)
    func[1].set_title('БПУ')
    func[1].grid(True)

    func[2].plot(x, reverse_transform)
    func[2].set_title('Обратное БПУ')
    func[2].grid(True)

    function_values_dut = list(map(lambda i: _fun(i), x))
    transform_dut = dut(function_values_dut)
    reverse_transform_idut = idut(transform_dut)

    func[3].plot(x, transform_dut)
    func[3].set_title('ДПУ')
    func[3].grid(True)

    func[4].plot(x, reverse_transform_idut)
    func[4].set_title('Обратное ДПУ')
    func[4].grid(True)

    plt.show()


if __name__ == '__main__':
    transformations()