import cv2
import numpy as np
from create_dir import CreateDir
import os


class ClassicalResize:
    __folder_name_and_size_dict = {"960x640": (960, 640), "400x400": (400, 400), "320x320": (320, 320),
                                   "200x200": (200, 200),
                                   "100x100": (100, 100), "50x50": (50, 50)}

    def __init__(self, img_path: str):
        self.img = cv2.imread(img_path, cv2.IMREAD_COLOR)
        self.img_path = img_path
        self.img_dir = os.path.dirname(img_path)
        self.file_name = os.path.splitext(os.path.basename(img_path))[0]

    def create_dirs_and_imgs(self):
        self.__create_dir()
        for dir_name, size in self.__folder_name_and_size_dict.items():
            resized_img = cv2.resize(self.img, size)
            new_img_path = 'C:/test3333' + '/' + dir_name + '/' + self.file_name
            print(new_img_path + '.png')
            cv2.imwrite(new_img_path + '.png', resized_img)

    def __create_dir(self):
        CreateDir(self.__folder_name_and_size_dict).create_dir()


imgs = ["900065", "900066", "900067", "900068", "900069", "900070"]

for img in imgs:
    test11 = ClassicalResize('./' + img + '.jpg').create_dirs_and_imgs()
