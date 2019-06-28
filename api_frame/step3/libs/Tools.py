import requests

# login_data = {
#     'email': '13587652131',
#     'user_pwd': 'U1BIVWp0dXlqYUFkdVpvU2hpYWdBZlBJZHlQUEtMRE1KcHZ0VmlsQUhtYnNrZXdMREElMjV1NjVCOSUyNXU3RUY0amsxNDcyNTglMjV1OEY2RiUyNXU0RUY2',
#     'ajax': '1',
# }
class BaseHttp(object):
    host = 'http://localhost/'

    # post请求方式
    def post_data(self,url,data,icon=1,*abs,**kwargs):

        url = '{}{}'.format(self.host,url)
        if icon == 1:
            result = requests.post(url=url,data=data,*abs,**kwargs)
        elif icon == 2:
            result = requests.post(url=url,files=data,*abs,**kwargs)
        return result

    # get请求方式
    def get_data(self,url,data,icon=1,*abs,**kwargs):
        url = '{}{}'.format(self.host, url)
        if icon == 1:
            result = requests.get(url=url,params=data,*abs,**kwargs)
        return result

# if __name__ == '__main__':
#     run = BaseHttp()
#     run.post_data('index.php?ctl=user&act=dologin',login_data)

