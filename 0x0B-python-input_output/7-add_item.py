#!/usr/bin/python3
"""Add all arguments to a Python list, and then save them to a file"""
sys = __import__('sys')
load_from_json_file = __import__(6-load_from_json_file).load_from_json_file
save_to_json_file = __import__(5-save_to_json_file).save_to_json_file


if __name__ == '__main__':
    try:
        new_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        new_list = []
    new_list.extend(sys.argv[1:])
    save_to_json_file(new_list, "add_item.json")
