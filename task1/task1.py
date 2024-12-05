import argparse
import math


def lcm(a, b):
    """Формула для нахождения наименьшего общего кратного (least common multiple)"""
    return abs(a * b) // math.gcd(a, b)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int, help='N: целое число, больше 0')
    parser.add_argument('m', type=int, help='M: целое число, больше 1')
    args = parser.parse_args()
    n = args.n
    if n < 1:
        raise ValueError('N должно быть больше 0')
    m = args.m
    if m <= 1:
        raise ValueError('M должно быть больше 1')

    # массив из всех цифр числа n
    c = [str(i) for i in range(1, n+1)] * int(lcm(n, m-1) / n)
    # берем из него все цифры с шагом окна m-1
    print(''.join(c[::m-1]))


if __name__ == '__main__':
    main()
