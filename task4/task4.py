import argparse
import statistics
import sys


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'f', type=str,
        help='f: путь до файла, который содержит массив с данными'
    )
    args = parser.parse_args()
    try:
        with open(args.f, 'r') as file:
            data = file.read().split('\n')
            data = [int(i) for i in data]
    except Exception as e:
        print(f"Ошибка при чтении файла '{args.f}': {e}")
        sys.exit(1)

    median_high = statistics.median_high(data)
    print(sum([abs(i - median_high) for i in data]))
    # Можно было бы проще сделать через Numpy, но не буду его устанавливать
    # print((abs(np.array(data) - round(np.median(data)))).sum())


if __name__ == '__main__':
    main()
