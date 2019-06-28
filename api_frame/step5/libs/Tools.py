
import requests
# login_data = {
#     'email': '13587652131',
#     'user_pwd': 'U1BIVWp0dXlqYUFkdVpvU2hpYWdBZlBJZHlQUEtMRE1KcHZ0VmlsQUhtYnNrZXdMREElMjV1NjVCOSUyNXU3RUY0amsxNDcyNTglMjV1OEY2RiUyNXU0RUY2',
#     'ajax': '1',
# }
class BaseHttp(object):

    host = 'http://localhost/'
    def http_send(self,url,method='post',*abs,**kwargs):
        url = '{}{}'.format(self.host, url)
        result = requests.request(method=method,url=url,*abs,**kwargs)
        return result
# if __name__ == '__main__':
#     run = BaseHttp()
#     result = run.http_send(url='index.php?ctl=user&act=dologin',data=login_data)
#     print(result.json())