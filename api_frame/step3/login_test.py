import requests
from libs.Tools import BaseHttp
# 建立登录接口函数
def apiLogin():
    run =BaseHttp()
    # 登录接口
    login_url = 'index.php?ctl=user&act=dologin'
    # 登录接口参数
    login_data  = {
        'email':'13587652131',
        'user_pwd':'U1BIVWp0dXlqYUFkdVpvU2hpYWdBZlBJZHlQUEtMRE1KcHZ0VmlsQUhtYnNrZXdMREElMjV1NjVCOSUyNXU3RUY0amsxNDcyNTglMjV1OEY2RiUyNXU0RUY2',
        'ajax':'1',
    }
    result = run.post_data(url=login_url,data=login_data)
    return result.json(),result.status_code

if __name__ == '__main__':
    a = apiLogin()
    print(a)
