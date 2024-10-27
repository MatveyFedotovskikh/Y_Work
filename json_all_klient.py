import json
import datetime
import os
import parser_client_arhiv_excel
import parser_client_excel


def clear_dowland_excel(path_dowland):
    dir_name = path_dowland
    test = os.listdir(dir_name)
    
    for item in test:
        
        timestamp = os.path.getmtime(f'{dir_name}/{item}')
        date_item = datetime.date.fromtimestamp(timestamp)
        date_now = datetime.date.today()
        if item.endswith(".csv") and  date_now == date_item:
            os.remove(fr'{dir_name}/{item}')


def start(
        path = r'Bot_for_Work_devoloper/Parser/parser_client_excel',
        path_arhiv = r'Bot_for_Work_devoloper/Parser/parser_client_arhiv_excel',
        path_dowland= r'C:\Users\mfudo\Downloads',
        name_json = r'client',
        name_json_arhiv = r'client_arhiv'
    ):
    if os.path.isfile(fr"Bot_for_Work_devoloper/json/all_client_{datetime.date.today()}.json"):
        with open(fr'Bot_for_Work_devoloper/json/all_client_{datetime.date.today()}.json', encoding='utf-8') as f:
            json_client = json.load(f)
        print('all client open')
        return json_client
    else:
        if os.path.isfile(f"{path}/json/client_{datetime.date.today()}.json"):
            with open(f'{path}/json/client_{datetime.date.today()}.json', encoding='utf-8') as f:
                json_client = json.load(f)
            print('client open')
        else:
            clear_dowland_excel(path_dowland)
            parser_client_excel.start(path = path, path_dowland = path_dowland, name_json= name_json)
            with open(f'{path}/json/client_{datetime.date.today()}.json', encoding='utf-8') as f:
                json_client = json.load(f)
            print('client open')

        if os.path.isfile(f'{path_arhiv}/json/client_arhiv_{datetime.date.today()}.json'):
            with open(f'{path_arhiv}/json/client_arhiv_{datetime.date.today()}.json', encoding='utf-8') as f:
                json_client_arhiv = json.load(f)
            print('arhiv client open')
        else:
            clear_dowland_excel(path_dowland)
            parser_client_arhiv_excel.start(path = path_arhiv, path_dowland = path_dowland, name_json= name_json_arhiv)
            with open(f'{path_arhiv}/json/client_arhiv_{datetime.date.today()}.json', encoding='utf-8') as f:
                json_client_arhiv = json.load(f)
            print('arhiv client open')

        json_all_client = {}


        for i in json_client.keys():
            json_all_client[i] = json_client[i]
            json_all_client[i]['arhiv'] = 'Активне'
        for i in json_client_arhiv.keys():
            json_all_client[i] = json_client_arhiv[i]
            json_all_client[i]['arhiv'] = 'Архив'

        with open(fr'Bot_for_Work_devoloper/json/all_client_{datetime.date.today()}.json', 'w', encoding='utf-8') as f:
            json.dump(json_all_client, f, ensure_ascii=False, indent=4)
        print('all client open')
        return json_all_client

# start(path = r'Bot_for_Work_devoloper/Parser/parser_client_excel',
#     path_arhiv = r'Bot_for_Work_devoloper/Parser/parser_client_arhiv_excel',
#     path_dowland= r'Bot_for_Work_devoloper/Parser',
#     name_json = r'Client',
#     name_json_arhiv = r'client_arhiv')


    


