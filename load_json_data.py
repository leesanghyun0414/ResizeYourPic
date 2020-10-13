import os
import json


class JsonData:

    def __init__(self, json_path):
        """

        Parameters
        ----------
        json_path : str
            JSONファイルのパスを文字列で受け取る
        """
        self.json_data_open = open(json_path, 'r', encoding="utf-8_sig")
        self.json_data = json.load(self.json_data_open)
        self.json_data_open.close()

    def get_item(self):
        """

        Returns
        -------
        self.json_data : Dict
            JSONデータをDict型で返す
        """
        return self.json_data

    def get_key(self):
        """

        Returns
        -------
        self.json_data.keys() : Any
            JSONデータのkeyをリストで返す
        """
        return self.json_data.keys()

    def get_value(self):
        """

        Returns
        -------
        self.json_data.values() : Any
            JSONデータのvalueをリストで返す
        """
        return self.json_data.values()
