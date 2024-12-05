import argparse
import json
import sys


def read_file(filepath):
    """Функция для чтения содержимого файла."""
    with open(filepath, 'r') as f:
        return f.read()


def fill_template(template: dict, data: dict):
    if 'id' in template.keys() and 'value' in template.keys():
        value = data.get(template['id'], None)
        if value is not None:
            template['value'] = value

    for value in template.values():
        if isinstance(value, list):
            for item in value:
                fill_template(item, data)
        if isinstance(value, dict):
            fill_template(value, data)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'f1', type=str,
        help='f1: путь до файла, который содержит результаты прохождения тестов с уникальными id'
    )
    parser.add_argument(
        'f2', type=str,
        help='f2: путь до файла, который содержит структуру для построения отчета на основе прошедших тестов'
    )
    parser.add_argument(
        'f3', type=str,
        help='f2: путь до файла, в который записывается результат'
    )
    args = parser.parse_args()
    file_path_1 = args.f1
    file_path_2 = args.f2
    file_path_3 = args.f3

    try:
        values = json.loads(read_file(file_path_1))
    except Exception as e:
        print(f"Ошибка при чтении файла '{file_path_1}': {e}")
        sys.exit(1)

    try:
        tests = json.loads(read_file(file_path_2))
    except Exception as e:
        print(f"Ошибка при чтении файла '{file_path_2}': {e}")
        sys.exit(1)

    data = {item['id']: item['value'] for item in values['values']}

    fill_template(tests, data)

    try:
        with open(file_path_3, 'w') as file:
            json.dump(tests, file, indent=2)
    except Exception as e:
        print(f"Ошибка при записи результатов '{file_path_2}': {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
