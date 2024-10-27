import os
from datetime import date
def start(path, path_dowland):
    dir_name = path_dowland
    new_dir_name = fr'{path}/excel'

    test = os.listdir(new_dir_name)
    for item in test:
        if item.endswith(".csv"):
            os.remove(fr'{new_dir_name}/{item}')

    test = os.listdir(dir_name)
    for item in test:
        if item.endswith(".csv"):
            timestamp = os.path.getmtime(f'{dir_name}/{item}')
            date_item = date.fromtimestamp(timestamp)
            date_now = date.today()
            if date_now == date_item:
                os.rename(fr'{dir_name}/{item}',f'{new_dir_name}/{item}')
        
        
    

