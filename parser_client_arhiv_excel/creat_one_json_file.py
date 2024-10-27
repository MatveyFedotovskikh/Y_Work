import json
import os
from datetime import date

def start(path, name_json):
    len_sum = 0
    dir_name = fr"{path}/json_excel"
    test = os.listdir(dir_name)
    number_file = 0
    all_json = {}
    for item in test:
        number_file += 1
        if item.endswith(".json"):
            with open(fr'{dir_name}/{item}', encoding='utf-8') as f:
                jsonf = json.load(f)
            for item in jsonf.keys():
                all_json[item] = jsonf[item]
                len_sum += len(jsonf.keys())

    with open(fr'{path}/json/{name_json}_{date.today()}.json', 'w', encoding='utf-8') as f:
        json.dump(all_json, f, ensure_ascii=False, indent=4)
    

