import unittest
from po.myp2p.prepay import Prepay
from libs.Tools import VerifyClass

class TestPrepayApi(VerifyClass):

    def setUp(self):
        self.p = Prepay()

    def test_prepay_success_001(self):
        result = self.p.apiPrepay()
        self.verify_code(result,200)
        self.verify_html(result,'878733')

if __name__ == '__main__':
    unittest.main()