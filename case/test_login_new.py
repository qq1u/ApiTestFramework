# @Time    : 2020/3/27 上午 11:27
# @Author  : Hugh
# @email   : 609799548@qq.com


from parameterized import parameterized

from case.base import Base
from tools.operator_json import OperatorJson


class TestLogin(Base):
    @parameterized.expand([(data['case_number'], data) for data in OperatorJson.get_cases('login.json')])
    def test_login(self, _, case):
        self.run_case('login', case)


if __name__ == '__main__':
    pass