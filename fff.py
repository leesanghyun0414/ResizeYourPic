import numpy as np
import cv2
import fffff as main
import os

dir_path = main.dir_path
test_path1 = 'abc'
test_path2 = 'def'
print(os.path.join(dir_path, test_path1, test_path2))

print(os.getcwd())
print(os.listdir(os.getcwd()))
