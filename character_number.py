import os
from load_json_data import JsonData
from collections.abc import Sequence
def get_character_num(character_name, id_type= "num") -> Sequence:
    file_name = "chara.json"
    json_data = JsonData(file_name)
    json_data_dict = json_data.get_items()
    if character_name in json_data_dict.keys():
        return json_data_dict[character_name][id_type]
    else:
        return None
