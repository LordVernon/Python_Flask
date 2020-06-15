import json


filename = "users.json"


def write(user_data: dict):
    f = open(filename, 'w', encoding="UTF-8")
    # f.write(json.dumps(user_data))
    json.dump(user_data, f)
    f.close()


def read() -> dict:
    f = open(filename)
    data = json.load(f)
    f.close()
    return data
