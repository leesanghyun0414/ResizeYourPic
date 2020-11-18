import shutil
from typing import Any

import cv2
import glob
import os

import open_cv_jp as cv2_jp
import character_number


def get_file_name(file_path) -> str:
    """
    Parameters
    ----------
    file_path : str
        this path is including the file name

    Returns
    -------
    str
        return filename without extension
    """

    return os.path.splitext(os.path.basename(file_path))[0]


def background_transparency(img_path) -> Any:
    """

    Parameters
    ----------
    img_path : str
        画像のパス

    Returns
    -------
    processing_img : buffer
        白の部分[RGB(255, 255, 255)]を透明化した画像bufferを返す
    """

    processing_img = cv2_jp.image_read(img_path, cv2.IMREAD_UNCHANGED)

    return processing_img


# value : tuples
#   画像のサイズ
folder_name_and_size_dict = {"640x640": (640, 640), "400x400": (400, 400), "320x320": (320, 320), "200x200": (200, 200),
                             "100x100": (100, 100), "50x50": (50, 50)}
read_file_type = 'png'
save_file_type = 'png'
dir_path_list = ['C:/test222/after_evolution/', 'C:/test222/before_evolution/']

for dir_path in dir_path_list:

    # フォルダーにあるpngファイルのパスをすべて読み取ってpathに一つずつ格納する
    for path in glob.glob(os.path.join(dir_path, f'*.{read_file_type}')):

        skillsoul_string = 'スキルソウル'
        file_name = get_file_name(path)
        if 'after_evolution' in dir_path and skillsoul_string not in file_name:
            id_type = 'num_evolutions'
        elif 'before_evolution' in dir_path and skillsoul_string not in file_name:
            id_type = 'num'
        elif skillsoul_string in file_name:
            id_type = 'skillsoul'
        else:
            id_type = None

        # フォーマットが違う場合はループを抜ける
        if id_type is None:
            print("フォーマットを確認してください。")
            continue

        file_name_without_skillsoul: str = file_name.split(skillsoul_string)[0]
        character_folder_path: str = os.path.join(dir_path, file_name)

        # すでにフォルダーが存在するか判定する
        if skillsoul_string in file_name:
            file_num = character_number.get_character_num(file_name.split(skillsoul_string)[0], id_type)
        else:
            file_num = character_number.get_character_num(file_name.split('アップ')[0], id_type)
        file_num_female = file_num.replace('5', '4', 1)

        # スキルソウルがファイル名に含まれなかった場合
        if not os.path.exists(dir_path + file_name) and skillsoul_string not in file_name:
            os.mkdir(dir_path + file_name)
        elif os.path.exists(dir_path + file_name_without_skillsoul) and not os.path.exists(
                dir_path + file_name_without_skillsoul + "/" + skillsoul_string):
            os.mkdir(dir_path + file_name_without_skillsoul + "/" + skillsoul_string)
        elif not os.path.exists(dir_path + file_name_without_skillsoul):
            os.mkdir(dir_path + file_name.split(skillsoul_string)[0])
            os.mkdir(dir_path + file_name.split(skillsoul_string)[0] + "/" + skillsoul_string)
        img = background_transparency(path)

        # フォルダ名と画像サイズのdictをループさせる
        for folder_name, img_size in folder_name_and_size_dict.items():
            numbering_folder = os.path.join(character_folder_path, folder_name)
            if 'アップ' not in file_name and skillsoul_string not in file_name and (
                    folder_name == '640x640' or folder_name == '320x320'):
                img = cv2.resize(img, img_size)
                if (not os.path.exists(numbering_folder)) and skillsoul_string not in file_name:
                    os.mkdir(numbering_folder)
                    sizing_dir_path = numbering_folder

                    # file_numが5桁未満の場合はファイル名先頭を0で埋める
                    if int(file_num) < 10000:
                        cv2_jp.imwrite(sizing_dir_path + "/" + "0" + file_num + f'.{save_file_type}', img)
                    elif int(file_num) < 1000:
                        cv2_jp.imwrite(sizing_dir_path + "/" + "00" + file_num + f'.{save_file_type}', img)
                    elif int(file_num) < 100:
                        cv2_jp.imwrite(sizing_dir_path + "/" + "000" + file_num + f'.{save_file_type}', img)
                    elif int(file_num) < 10:
                        cv2_jp.imwrite(sizing_dir_path + "/" + "0000" + file_num + f'.{save_file_type}', img)
                    else:
                        cv2_jp.imwrite(sizing_dir_path + "/" + file_num + f'.{save_file_type}', img)

                    for num in range(1, 11):
                        if num != 10:
                            cv2_jp.imwrite(sizing_dir_path + "/" + file_num + "0" + str(num) + '.png', img)
                        else:
                            cv2_jp.imwrite(sizing_dir_path + "/" + file_num + str(num) + '.png', img)

            # 50x50, 100x100, 200x200, 400x400のサイズはロゴを付ける
            elif 'アップ' in file_name and 'ロゴ無し' not in file_name and skillsoul_string not in file_name \
                    and folder_name != '640x640' \
                    and folder_name != '320x320':
                img = cv2.resize(img, img_size)
                if (not os.path.exists(numbering_folder)) and skillsoul_string not in file_name:
                    os.mkdir(numbering_folder)
                    sizing_dir_path = numbering_folder
                    cv2_jp.imwrite(sizing_dir_path + "/" + "0" + file_num + '.png', img)
                    for num in range(1, 11):
                        if num != 10:
                            cv2_jp.imwrite(sizing_dir_path + "/" + file_num + "0" + str(num) + '.png', img)
                        else:
                            cv2_jp.imwrite(sizing_dir_path + "/" + file_num + str(num) + '.png', img)
            # 320x320サイズにはロゴ無しイメージを保存する
            # elif ('アップ' and 'ロゴ無し') in file_name and folder_name == '320x320':
            #     img = cv2.resize(img, img_size)
            #     if (not os.path.exists(numbering_folder)) and "スキルソウル" not in file_name:
            #         os.mkdir(numbering_folder)
            #         sizing_dir_path = numbering_folder
            #         cv2_jp.imwrite(sizing_dir_path + "/" + "0" + file_num + '.png', img)
            #         for num in range(1, 11):
            #             if num != 10:
            #                 cv2_jp.imwrite(sizing_dir_path + "/" + file_num + "0" + str(num) + '.png', img)
            #             else:
            #                 cv2_jp.imwrite(sizing_dir_path + "/" + file_num + str(num) + '.png', img)
            # ファイル名にスキルソウルが入っている場合
            elif skillsoul_string in file_name:
                img = cv2.resize(img, img_size)
                if not os.path.exists(
                        dir_path + file_name.split(skillsoul_string)[0] + "/" + skillsoul_string + "/" + folder_name):
                    os.mkdir(
                        dir_path + file_name.split(skillsoul_string)[0] + "/" + skillsoul_string + "/" + folder_name)
                    sizing_dir_path = dir_path + file_name.split(skillsoul_string)[
                        0] + "/" + skillsoul_string + "/" + folder_name
                    for num in range(1, 6):
                        cv2_jp.imwrite(sizing_dir_path + "/" + file_num + "0" + str(num) + '.png', img)
                        cv2_jp.imwrite(sizing_dir_path + "/" + file_num_female + "0" + str(num) + '.png', img)
        # 作成したフォルダーをキャラクターフォルダーに結合する
        if 'ロゴ無し' in file_name or 'アップ' in file_name:
            files = os.listdir(dir_path + file_name)
            files_dir = [f for f in files if os.path.isdir(os.path.join(dir_path + file_name, f))]
            for folder in files_dir:
                shutil.move(dir_path + file_name + '/' + folder, dir_path + file_name.split('アップ')[0])
            # 移動した後の空フォルダーを削除する
            shutil.rmtree(dir_path + file_name)
