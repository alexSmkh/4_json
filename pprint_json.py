import json
import sys
from json.decoder import JSONDecodeError


def load_data(file_name):
    try:
        with open(file_name, 'r', encoding='utf8') as file_handler:
            return json.load(file_handler)
    except IOError:
        print('File not found')
    except JSONDecodeError:
        print('The file must be a json format')


def pretty_print_json(data_for_formatting):
    return json.dumps(data_for_formatting, indent=5, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        data_from_file = load_data(file_path)
        if data_from_file:
            print(pretty_print_json(data_from_file))
    except IndexError:
        print('You forgot to enter the file name.')
