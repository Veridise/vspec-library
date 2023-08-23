import json


def write_json(file_name, data):
    with open(file_name, "wt", encoding="utf-8") as file_handle:
        json.dump(data, file_handle, indent=2)


def read_json(file_name):
    with open(file_name, "rt", encoding="utf-8") as file_handle:
        return json.load(file_handle)


def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file_handle:
        return file_handle.read()


def write_file(file_name, data):
    with open(file_name, "wt", encoding="utf-8") as file_handle:
        file_handle.write(data)
