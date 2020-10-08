import cv2
import glob
import os
import numpy as np
import sys


# 日本語ファイル名も読見とれるようにするためにOverride
def image_read(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None


# 日本語ファイル名も読見とれるようにするためにOverride
def imwrite(filename, img, params=None):
    """
    Parameters
    ----------
    filename : str
        ファイル名文字列
    img : str
        画像ファイルのパス
    params:

    Returns
    -------
    bool
        True if successful, False otherwise.

    Notes
    -----
    params Format-specific parameters encoded as pairs (paramId_1, paramValue_1, paramId_2, paramValue_2, ... .)
    see cv::ImwriteFlags
    """

    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)

        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def get_file_name(file_path) -> str:
    """
    指定されたファイルパスからファイル名だけを返す
    :param file_path:
    :return: file_name
    """
    return os.path.splitext(os.path.basename(file_path))[0]


size_dict = {"640x640": (640, 640), "400x400": (400, 400), "320x320": (320, 320), "200x200": (200, 200),
             "100x100": (100, 100), "50x50": (50, 50)}
read_file_type = 'jpg'
save_file_type = 'png'
dir_path = 'C:/test222/'
for path in glob.glob(os.path.join(dir_path, f'*.{read_file_type}')):
    file_name = get_file_name(path)
    if not os.path.exists(dir_path + file_name) and 'スキルソウル' not in file_name:
        os.mkdir(dir_path + file_name)
    elif os.path.exists(dir_path + file_name.split("スキルソウル")[0]):
        os.mkdir(dir_path + file_name.split("スキルソウル")[0] + "/" + "スキルソウル")
    elif not os.path.exists(dir_path + file_name.split("スキルソウル")[0]):
        os.mkdir(dir_path + file_name.split('スキルソウル')[0])
        os.mkdir(dir_path + file_name.split('スキルソウル')[0] + "/" + "スキルソウル")

    img = image_read(path)
    file_num = input(f"{file_name} の附番を入力してください")
    file_num_female = file_num.replace('5', '4', 1)
    print(file_num_female)
    for size_folder, size_file in size_dict.items():
        img = cv2.resize(img, size_file)
        if (not os.path.exists(dir_path + file_name + "/" + size_folder)) and "スキルソウル" not in file_name:
            os.mkdir(dir_path + file_name + "/" + size_folder)
            sizing_dir_path = dir_path + file_name + "/" + size_folder
            for i in range(0, 11):
                imwrite(sizing_dir_path + "/" + file_num + "0" + str(i) + '.png', img)
        else:
            os.mkdir(dir_path + file_name.split('スキルソウル')[0] + "/" + "スキルソウル" + "/" + size_folder)
            sizing_dir_path = dir_path + file_name.split('スキルソウル')[0] + "/" + "スキルソウル" + "/" + size_folder
            for i in range(1, 6):
                imwrite(sizing_dir_path + "/" + file_num + "0" + str(i) + '.png', img)
                imwrite(sizing_dir_path + "/" + file_num_female + "0" + str(i) + '.png', img)

# img = cv2.imread("C:/test222/aaa.jpg")  # read image
# img = cv2.resize(img, (300, 300))
# file_name = "300x300"
# cv2.imwrite(f"{dir_path}{file_name}.{read_file_type}", img, None)
