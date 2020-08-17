from bottle import run, get

from bll.user_bll import UserBll
from utils.config import Config
from utils.http_utils import HttpUtils


@get('/user')
def get():
    user_bll = UserBll()
    users = user_bll.get_users()

    if users is None:
        return HttpUtils.response_not_found()
    else:
        return HttpUtils.response_ok(users)


run(host='localhost', port=Config.HOST_PORT, debug=True)
