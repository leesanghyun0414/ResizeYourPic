import numpy as np
from pathlib import Path
import os
import shutil as stl
from load_json_data import JsonData

from_dir = r"C:\Users\GRIT_B\Downloads\桜"
to_dir = r"C:\Users\GRIT_B\Downloads\to"
dir_names = ['50x50', "100x100", "200x200", "320x320", "400x400", "640x640", "960x640"]
words_ids = {
    "120000001": "天上天下唯我独尊",
    "120000003": "サツにチンコロしたんはおどれらか",
    "120000004": "頼むワシを男にしてくれ",
    "120000005": "ぶちかますぞわれ",
    "120000007": "お帰りなさいませご主人様",
    "120000008": "あっ…---ん…---もうっ！耳、ﾌｰｯてするの、禁止ッ！"
}

avatar_json = JsonData(json_path="./resizing_images.json")
avatar_names = avatar_json.get_key()
avatars = avatar_json.get_items()

pp = [Path(from_dir + "/" + avatar_name) for avatar_name in avatar_names]

words_ids_swap = {v: k for k, v in words_ids.items()}
dirs = os.listdir(from_dir)

p = Path(from_dir)

to_p = Path(to_dir)

# for p_child in pp:
#     p_child.mkdir(exist_ok=True)

tests = p.glob("**/*.png")


# print(list(tests))


def get_file_name(parent_dir_name) -> str:
    return avatars[parent_dir_name] + ".png"


# for test in tests:
#     print(test)
#     parent_name = test.parent
#     file_name_without_extensions = test.stem
#     file_name = test.name
#     new_file_name = get_file_name(file_name_without_extensions)
#     old_path = test
#     new_path = Path(str(test.parent) + "/" + new_file_name)
#     print("old : ", old_path)
#     print("new : ", new_path)

# old_path.rename(new_path)

p2 = Path(r"C:\Users\GRIT_B\Downloads\案山子")
p2_glob = p2.glob("**/*.png")

for p2_path in p2_glob:
    old_name = p2_path
    new_file_name = "04061.png"
    new_name = str(old_name.parent) + "/" + new_file_name
    old_name.rename(new_name)

#
# for test in tests:
#     parent_name = test.parts[-2]
#     file_name = test.stem
#     new_file_name = get_file_name(parent_name)
#     print(new_file_name)
#     target_dir_path = to_p.joinpath(file_name)
#     # stl.move(test, target_dir_path.joinpath(new_file_name))
#     stl.copymode(test, target_dir_path.joinpath(new_file_name))
