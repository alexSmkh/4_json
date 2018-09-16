import json
from sys import argv


def load_data(file_path):
    with open(file_path, 'r', encoding='utf8') as file_handler:
        return json.load(file_handler)


def pretty_print_json(json_data):
    print(json.dumps(json_data, indent=5, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    file_path = input('Укажите путь к файлу: ')
    json_data = load_data(file_path)
    pretty_print_json(json_data)
