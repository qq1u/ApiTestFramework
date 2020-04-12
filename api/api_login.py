# @Time    : 2020/3/26 下午 01:02
# @Author  : Hugh
# @email   : 609799548@qq.com


from tools.util import get_full_url, Request

request = Request()


def login(data):
    return request.post(get_full_url('login.json'), json=data)
