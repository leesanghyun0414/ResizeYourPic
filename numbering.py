import os
import shutil
import cv2
import numpy as np
import shutil
import zipfile


def make_dirs(names: list[str], paths: list[str]) -> None:
    for path in paths:
        for name in names:
            print(path + "/" + name)
            os.makedirs(path + "/" + name, exist_ok=True)


#
#
# img_paths = [r"C:\Users\GRIT_B\Desktop\ab\a\640x640\70013001.png", r"C:\Users\GRIT_B\Desktop\ab\b\640x640\70013201.png"]
# pic_nums = [70013001, 70013201]
# base_paths = [r"C:\Users\GRIT_B\Desktop\ab\a", r"C:\Users\GRIT_B\Desktop\ab\b"]
# dir_names = ["50x50", "100x100", "200x200", "400x400", "640x640"]
# sizes = [(50, 50), (100, 100), (200, 200), (400, 400), (640, 640)]
# imgs = [cv2.imread(img_path, cv2.IMREAD_UNCHANGED) for img_path in img_paths]
#
# for pic_num, base_path, img in zip(pic_nums, base_paths, imgs):
#     for dir_name, size in zip(dir_names, sizes):
#         add_num = 0
#         resized_img = cv2.resize(img, size)
#         new_path = base_path + "/" + dir_name + "/"
#         for i in range(1, 21):
#             print(new_path + f"{pic_num + add_num}.png")
#             cv2.imwrite(new_path + f"{pic_num + add_num}.png", resized_img)
#             add_num += 1

sizes = (50, 100, 320, 400, 640)
img_path = r"C:\60006401.png"
pic_num = 70030001
zip_target_dir_paths: list[str] = []
zip_name = "stickers"
root_dir = r"C:"

img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

for size in sizes:
    add_num = 0
    dir_path = rf"C:\{size}X{size}"

    resized_img = cv2.resize(img, (size, size))

    os.makedirs(dir_path, exist_ok=True)
    zip_target_dir_paths.append(dir_path)

    for i in range(20):
        new_path = rf"C:\{size}X{size}\{pic_num + add_num}.png"
        cv2.imwrite(new_path, resized_img)
        add_num += 1


# print(shutil.make_archive(zip_name, 'zip', root_dir=r"C:\Users\GRIT_B\Desktop\stickers",base_dir=))

# with zipfile.ZipFile(rf"C:\{zip_name}",'w') as new_zip:
#     for zip_target, size in zip(zip_target_dir_paths, sizes):
#         new_zip.write(rf"C:\")
