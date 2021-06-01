import os


class CreateDir:
    """
test
    """
    __base_path = "C:/test3333/"

    def __init__(self, img_size_strings: list or dict):
        self.img_size_strings = img_size_strings
        self.dir_name_from_img_size = self.__get_size_texts(self.img_size_strings)

    def __get_size_texts(self, img_size_strings):
        img_size_strings_type = self.__type_selector(img_size_strings)

        if img_size_strings_type is dict:
            return self.img_size_strings.keys()
        elif img_size_strings_type is list:
            return self.img_size_strings

    @staticmethod
    def __type_selector(variable: any):

        return type(variable)

    def create_dir(self):
        for dir_name in self.dir_name_from_img_size:
            os.makedirs(self.__base_path + dir_name, exist_ok=True)


test = CreateDir({"1": 1, "2": 1})
print(test.dir_name_from_img_size)
test.create_dir()
