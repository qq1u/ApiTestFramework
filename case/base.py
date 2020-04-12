# @Time    : 2020/3/27 上午 11:07
# @Author  : Hugh
# @email   : 609799548@qq.com

import unittest

from tools.util import check
from tools.setup_teardownn import functions
from tools.operator_json import OperatorJson
from api import functions as api_interfaces


class Base(unittest.TestCase):

    @classmethod
    def assert_response(cls, assert_dict, r):
        for value in assert_dict.values():
            if value:
                for except_key in value:
                    assert value[except_key] == r.get(except_key)

    @classmethod
    def run_arg(cls, interface, arg):
        print(f'案例: {arg["desc"]}')

        if arg.get('setups'):
            for setup in arg['setups']:
                functions[setup]()

        require = {k: OperatorJson.get_require()[k] for k, v in arg.get('request').get('data').items() if check(v)}

        request_data = arg['request']['data']

        if require:
            request_data.update(require)

        r = api_interfaces[interface](request_data)

        print('<request>\n' + '\turl:', r.url)
        print('\tdata:', r.request.body.decode('unicode_escape'))
        print('\theaders:', r.request.headers)

        print('<response>\n' + '\tdata:' + str(r.json()))
        print('\theaders:', r.headers, '\n\n')

        if arg.get('teardowns'):
            for teardown in arg['teardowns']:
                functions[teardown]()

        cls.assert_response(arg.get('assert'), r.json())

    @classmethod
    def run_case(cls, api, case):
        print('-' * 30, '测试用例[CASE]：', case['title'], '-' * 30, '\n\n')
        if case.get('setups'):
            for setup in case['setups']:
                functions[setup]()

        for arg in case.get('args'):
            cls.run_arg(api, arg)

        if case.get('teardowns'):
            for teardown in case['teardowns']:
                functions[teardown]()


if __name__ == '__main__':
    pass