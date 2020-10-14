import os
from load_json_data import JsonData

def get_character_num(character_name):
    file_name = "chara.json"
    json_data = JsonData(file_name)
    json_data_dict = json_data.get_item()
    if character_name in json_data_dict.keys():
        return json_data_dict[character_name]['num']
    else:
        return None
