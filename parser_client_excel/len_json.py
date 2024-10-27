import json
from datetime import date

def start(path, name_json):
    with open(fr'{path}/json/{name_json}_{date.today()}.json', encoding='utf-8') as f:
        jsonf = json.load(f)

    print(len(jsonf.keys()))

