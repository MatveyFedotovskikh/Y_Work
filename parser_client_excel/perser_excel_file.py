
import csv
import json
import pandas as pd
import os

def make_json(csvFilePath, jsonFilePath):
    with open(csvFilePath,'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        first_line = []
        jsonf = {}
        for line in reader:
            if first_line == []:
                first_line = line
            else:
                info_in_line = {}
                
                for columns_in_line in range(len(line)):
                    info_in_line[first_line[columns_in_line]] = line[columns_in_line]
                jsonf[line[0]] = info_in_line
    with open(jsonFilePath, 'w', encoding='utf-8') as f:
        json.dump(jsonf, f, ensure_ascii=False, indent=4)




def start(path):
    dir_name = fr"{path}/excel"
    json_dir_name = fr'{path}/json_excel'
    test = os.listdir(json_dir_name)
    for item in test:
        if item.endswith(".json"):
            os.remove(f'{json_dir_name}/{item}')
    test = os.listdir(dir_name)
    number_file = 0
    for item in test:
        number_file += 1
        if item.endswith(".csv"):
            os.rename(fr'{path}/excel/{item}', fr'{path}/excel/{number_file}.csv')

            csvFilePath = fr'{dir_name}/{number_file}.csv'
            jsonFilePath = fr'{json_dir_name}/test{number_file}.json'
            make_json(csvFilePath, jsonFilePath)
