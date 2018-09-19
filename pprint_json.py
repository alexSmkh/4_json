import json
import sys
from json.decoder import JSONDecodeError


def load_data(file_name):
    with open(file_name, 'r', encoding='utf8') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data_for_formatting):
    print(json.dumps(data_for_formatting, indent=5, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        data_from_file = load_data(file_path)
        if data_from_file:
            pretty_print_json(data_from_file)
    except IndexError:
        print('You forgot to enter the file name.')
    except IOError:
        print('File not found')
    except JSONDecodeError:
        print('The file must be a json format')
