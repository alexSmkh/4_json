import json
import sys
from json.decoder import JSONDecodeError


def load_data(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8-sig') as file_handler:
            return json.load(file_handler)
    except IOError:
        print_info_about_error('IOError')
    except JSONDecodeError:
        print_info_about_error('JSONDecodeError')


def pretty_print_json(data_for_formatting):
    return json.dumps(data_for_formatting, indent=5, sort_keys=True, ensure_ascii=False)


def print_info_about_error(exception):
    probable_exceptions = {
        'IndexError': 'You forgot to enter the file name.',
        'IOError': 'File not found.',
        'JSONDecodeError': 'The file must be a json format.'}
    print(probable_exceptions.get(exception))


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        data_from_file = load_data(file_path)
        if data_from_file:
            print(pretty_print_json(data_from_file))
    except IndexError:
        print_info_about_error('IndexError')
