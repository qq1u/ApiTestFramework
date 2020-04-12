# @Time    : 2020/3/27 上午 11:43
# @Author  : Hugh
# @email   : 609799548@qq.com

from parameterized import parameterized

from case.base import Base
from tools.operator_json import OperatorJson


class TestEditUser(Base):
    @parameterized.expand([(data['case_number'], data) for data in OperatorJson.get_cases('edit_user.json')])
    def test_edit_user(self, _, case):
        self.run_case('edit_user', case)


if __name__ == '__main__':
    pass