from .parser_info                 import  start  as   parser_info             
from .excel_files_in_project      import  start  as   excel_files_in_project  
from .perser_excel_file           import  start  as   perser_excel_file       
from .create_one_json_file        import  start  as   create_one_json_file
from .len_json                    import  start  as   len_json

# path = r'parser_klient_excel'
# path_dowland= r'C:\Users\mfudo\Downloads'
# name_json = r'klient'

def start(path, path_dowland, name_json):
    parser_info()
    excel_files_in_project(path=path, path_dowland=path_dowland)
    perser_excel_file(path=path)
    create_one_json_file(path=path, name_json=name_json)
    len_json(path=path, name_json=name_json)



