import json
import argparse
import os


def load_data(file_name):
    if file_name.endswith('.json'):
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf8') as file_handler:
                return json.load(file_handler)
        else:
            print('File not found')
            exit()
    else:
        print('Incorrect data format')
        exit()


def get_arguments_from_console():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', type=str, help='file containing json for pretty print')
    args = parser.parse_args()
    return args


def pretty_print_json(json_file):
    return json.dumps(json_file, indent=5, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    args = get_arguments_from_console()
    json_file = load_data(args.file_name)
    print(pretty_print_json(json_file))
