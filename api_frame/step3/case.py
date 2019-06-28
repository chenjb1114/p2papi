import unittest
from login_test import apiLogin

class Testlogin(unittest.TestCase):
    def test_login_success(self):
        data,code = apiLogin()
        # 校验状态码
        self.assertEqual(code,200)
        # 校验返回文本信息
        self.assertEqual(data['info'],'成功登录')

if __name__ == '__main__':
    unittest.main()
