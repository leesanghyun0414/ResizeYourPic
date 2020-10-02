import numpy as np
import cv2


# Load your pic
class ReadPic:
    size_list = [[640, 640], [400, 400], [320, 320], [200, 200], [100, 100], [50, 50]]
    size_dict = {"640x640": [640, 640], "400x400": [400, 400]}

    def __init__(self):
        self.img = cv2.imread(self)

    def resizing(self):
        cv2.resize(self.img, (self.size_list[0][0], self.size_list[0][1]))
        resized_img = cv2.resize(self.img, (self.size_dict["640x640"]))
        cv2.imwrite('file_name', resized_img, None)


