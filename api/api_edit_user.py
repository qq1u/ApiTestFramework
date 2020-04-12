# @Time    : 2020/3/26 下午 04:14
# @Author  : Hugh
# @email   : 609799548@qq.com


from tools.util import get_full_url, Request

request = Request()


def edit_user(data):
    return request.put(get_full_url('edit_user.json'), json=data)
