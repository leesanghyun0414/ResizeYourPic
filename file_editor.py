from collections.abc import Iterable
import os
import glob


class FileEditor:

    def __init__(self, file_paths: Iterable[str]):
        self.file_paths = file_paths
        self.dir_names = [os.path.dirname(file_path) for file_path in self.file_paths]
        self.file_names = [os.path.basename(file_path) for file_path in self.file_paths]

    def add_num_left_all_file_name(self, add_num: int):
        for file_path, dir_name, file_name in zip(self.file_paths, self.dir_names, self.file_names):
            if file_name[0] == 0:
                new_file_name = "1" + file_name
            else:
                new_file_name = str(add_num) + file_name
            os.rename(file_path, f"{dir_name}/ {new_file_name}")


file_paths = glob.glob(r"C:\test222\after_evolution\test\**\*")

file_editor = FileEditor(file_paths=file_paths)
file_editor.add_num_left_all_file_name(10)
