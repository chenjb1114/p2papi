import unittest
import requests
#   Http统一请求
class BaseHttp(object):

    host = 'http://localhost/'
    def http_send(self,url,method='post',*abs,**kwargs):
        url = '{}{}'.format(self.host, url)
        result = requests.request(method=method,url=url,*abs,**kwargs)
        return result
# 校验类
class VerifyClass(unittest.TestCase):

    # 校验状态码
    def verify_code(self,result,v_code):
        self.assertEqual(result.status_code,v_code)

    # 校验某个html字段
    def verify_html(self,result,v_html):
        # 包含某个字段存在文本中
        self.assertIn(v_html,result.text)

    # 校验某个Json字段
    def verify_json(self,result,v_json):
        self.assertEqual(result.json(),v_json)


