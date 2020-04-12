# @Time    : 2020/3/26 下午 03:10
# @Author  : Hugh
# @email   : 609799548@qq.com


from tools.util import get_full_url, Request

request = Request()


def register(data):
    return request.post(get_full_url('register.json'), json=data)
