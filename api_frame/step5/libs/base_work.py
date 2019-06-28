from libs.Tools import BaseHttp
# 登录接口类
class LoginClass(BaseHttp):
    cookies = {
        'PHPSESSID':''
    }
    def apiLogin(self):
        # 登录接口
        login_url = 'index.php?ctl=user&act=dologin'
        # 登录接口参数
        login_data  = {
            'email':'13587652131',
            'user_pwd':'U1BIVWp0dXlqYUFkdVpvU2hpYWdBZlBJZHlQUEtMRE1KcHZ0VmlsQUhtYnNrZXdMREElMjV1NjVCOSUyNXU3RUY0amsxNDcyNTglMjV1OEY2RiUyNXU0RUY2',
            'ajax':'1',
        }
        result = self.http_send(method='post',url=login_url,data=login_data)
        pid = result.cookies['PHPSESSID']
        self.cookies['PHPSESSID'] = pid
        return result

if __name__ == '__main__':
    run = LoginClass()
    run.apiLogin()