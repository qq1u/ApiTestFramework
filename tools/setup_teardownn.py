# @Time    : 2020/3/26 下午 05:22
# @Author  : Hugh
# @email   : 609799548@qq.com
import random
import time

import api.api_login
from tools.operator_json import OperatorJson


def login():
    data = {
        "username": 'qiujiajin',
        'password': '123456'
    }
    r = api.api_login.login(data)
    require = {
        "userId": r.json().get('userId'),
        "token": r.json().get('token')
    }
    OperatorJson.touch_temp_json(require)
    return True


def delete():
    pass


def time_sleep():
    time.sleep(random.randint(0, 3))


functions = {
    'login': login,
    'delete': delete,
    'time': time_sleep
}