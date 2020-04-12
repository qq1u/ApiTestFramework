# @Time    : 2020/3/26 下午 05:49
# @Author  : Hugh
# @email   : 609799548@qq.com

import os
import re
import time
import logging
import unittest

import requests

from tools.operator_json import OperatorJson
from tools.HTMLTestRunner import HTMLTestRunner

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
API_PATH = os.path.join(BASE_PATH, 'api')
CASE_PATH = os.path.join(BASE_PATH, 'case')
DATA_PATH = os.path.join(BASE_PATH, 'data')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')


class Request:
    def __init__(self, headers=None):
        if headers is None:
            headers = {}
        self.headers = headers

    def request(self, method, url, params=None, data=None, json=None, **kwargs):
        try:
            return requests.request(method, url, headers=self.headers, params=params, data=data, json=json, **kwargs)
        except Exception as e:
            print(f'请求异常错误： {e.args}')

    def get(self, url, params=None, **kwargs):
        return self.request('get', url, params, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request('post', url, data=data, json=json, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request('put', url, data=data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request('delete', url,  **kwargs)


def get_logger(name):
    logger = logging.getLogger(name)

    handler1 = logging.StreamHandler()
    handler2 = logging.FileHandler(filename=os.path.join(LOG_PATH, get_today() + '.log'), encoding='utf-8')

    logger.setLevel(logging.DEBUG)
    handler1.setLevel(logging.WARNING)
    handler2.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(pathname)s - %(levelname)s - %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler1.setFormatter(formatter)
    handler2.setFormatter(formatter)

    logger.addHandler(handler1)
    logger.addHandler(handler2)

    return logger


def check(s):
    if isinstance(s, str):
        try:
            re.findall(r'^\${([^{}]+?)}$', s)[0]
        except IndexError:
            return False
        return True
    else:
        return False


def get_full_url(filename):
    """获取url"""
    host = OperatorJson.read_json('config.json').get('host')
    url = OperatorJson.get_config(filename).get('url')
    return host + url


def get_today(fmt='%Y-%m-%d'):
    return time.strftime(fmt)


logger = get_logger(__name__)


def main(title='接口自动化测试报告', description='描述信息'):
    logger.info('加载测试用例套件 --- start')
    suites = unittest.defaultTestLoader.discover(CASE_PATH, pattern='test_*.py')
    logger.info('加载测试用例套件 --- end')
    report = os.path.join(REPORT_PATH, get_today() + '.html')
    logger.info('start --- 执行测试用例 --- start')
    with open(report, 'wb') as f:
        HTMLTestRunner(stream=f, title=title, description=description).run(suites)
    logger.info('end --- 执行测试用例 --- end')


if __name__ == '__main__':
    print(BASE_PATH)
