import argparse
import math
import os
import sys


def read_file(filepath):
    """Функция для чтения содержимого файла."""
    with open(filepath, 'r') as f:
        return f.read()


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('f1', type=str, help='f1: путь до файла с координатами окружности')
    parser.add_argument('f2', type=str, help='f2: путь до файла с координатами точек')
    args = parser.parse_args()
    file_path_1 = args.f1
    file_path_2 = args.f2

    if not os.path.isfile(file_path_1):
        print(f"Ошибка: файл '{file_path_1}' не существует.")
        sys.exit(1)
    if not os.path.isfile(file_path_2):
        print(f"Ошибка: файл '{file_path_2}' не существует.")
        sys.exit(1)

    try:
        file_1 = read_file(file_path_1)
        circle_coordinates, radius = file_1.split('\n')
        circle_coordinates = [float(i) for i in circle_coordinates.split(' ')]
        radius = float(radius)
        if radius <= 0:
            print("Радиус окружности должен быть положительным числом.")
            sys.exit(1)

        file_2 = read_file(file_path_2)
        points = [[float(x) for x in i.split(' ')] for i in file_2.split('\n')]
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        sys.exit(1)

    for point in points[:100]: # Не больше 100 точек по условию
        distance = math.dist(circle_coordinates, point)
        if math.isclose(distance, radius):
            print('0')
        elif distance < radius:
            print('1')
        else:
            print('2')


if __name__ == '__main__':
    main()
