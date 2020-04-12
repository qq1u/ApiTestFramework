# @Time    : 2020/3/26 下午 12:49
# @Author  : Hugh
# @email   : 609799548@qq.com

from api.api_edit_user import edit_user
from api.api_login import login
from api.api_register import register


functions = {
    'edit_user': edit_user,
    'login': login,
    'register': register
}