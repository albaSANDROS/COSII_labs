from operations import Operations
import numpy as np
import matplotlib.pyplot as plt


def main():
    n = 8
    arguments = np.arange(0, n) * np.pi / 10
    function_values_1 = list(map(np.sin, arguments))
    function_values_2 = list(map(np.cos, arguments))

    basic_correlation = Operations.basic_function(function_values_1, function_values_2, 1)
    print('Basic correlation complexity: {}'.format(Operations.counter))
    basic_convolution = Operations.basic_function(function_values_1, function_values_2, -1)
    print('Basic convolution complexity: {}'.format(Operations.counter))

    fft_based_correlation = Operations.fft_based_function(function_values_1, function_values_2, 1)
    print('FFT-based correlation complexity: {}'.format(Operations.counter))
    fft_based_convolution = Operations.fft_based_function(function_values_1, function_values_2, -1)
    print('FFT-based convolution complexity: {}'.format(Operations.counter))

    _, represent = plt.subplots(3, 2)

    represent[0, 0].plot(arguments, function_values_1)
    represent[0, 0].set(title='First sequence')
    represent[0, 0].grid(True)

    represent[0, 1].plot(arguments, function_values_2)
    represent[0, 1].set(title='Second sequence')
    represent[0, 1].grid(True)

    represent[1, 0].plot(arguments, basic_correlation)
    represent[1, 0].set(title='Basic correlation')
    represent[1, 0].grid(True)

    represent[1, 1].plot(arguments, basic_convolution)
    represent[1, 1].set(title='Basic convolution')
    represent[1, 1].grid(True)

    represent[2, 0].plot(arguments, fft_based_correlation)
    represent[2, 0].set(title='FFT-based correlation')
    represent[2, 0].grid(True)

    represent[2, 1].plot(arguments, fft_based_convolution)
    represent[2, 1].set(title='FFT-based convolution')
    represent[2, 1].grid(True)

    plt.show()


if __name__ == '__main__':
    main()
