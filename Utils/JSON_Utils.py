import json


def get_json_field(filename, field):
    with open(filename, 'r') as file:
        jsonData = json.load(file)
        f = field
        return jsonData.get(f)
