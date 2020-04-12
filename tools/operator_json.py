# @Time    : 2020/3/26 下午 12:51
# @Author  : Hugh
# @email   : 609799548@qq.com


import os
import json


class OperatorJson:

    base_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data')

    @classmethod
    def read_json(cls, filename='login.json'):
        """
        读取json文件，返回 [{"config": {}}, {"case1"}, {"case2"}...]
        :param filename: 文件名
        :return: list
        """
        filename = os.path.join(cls.base_path, filename)
        with open(filename, encoding='utf-8') as f:
            data = json.load(f)
        return data

    @classmethod
    def get_config(cls, filename="login.json"):
        """
        读取case json文件，返回config
        :param filename: 文件名
        :return: dict {"config": ""}
        """
        return cls.read_json(filename)[0]['config']

    @classmethod
    def get_cases(cls, filename='login.json'):
        """
        读取case json文件，返回cases
        :param filename: 文件名
        :return: list [{'case'1}, {'case2'}]
        """
        return cls.read_json(filename)[1:]

    @classmethod
    def touch_temp_json(cls, content):
        with open(os.path.join(cls.base_path, 'temp.json'), 'w', encoding='utf-8') as f:
            json.dump(content, f)

    @classmethod
    def get_require(cls):
        try:
            data = cls.read_json('temp.json')
        except FileNotFoundError:
            data = {}
        return data


if __name__ == '__main__':
    print(OperatorJson.read_json('register.json'))