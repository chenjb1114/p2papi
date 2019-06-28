from libs.base_work import LoginClass
class Prepay(LoginClass):
    def apiPrepay(self):
        # 线下充值接口
        url = 'member.php?ctl=uc_money&act=incharge_done'
        # 线下充值传参数据
        recharge_data = {
            'check_ol_bl_pay':'on',
            'money':'300',
            'pingzheng':'',
            'memo':'878734',
            'payment':'5',
            'bank_id':'2',
        }
        # 登录
        self.apiLogin()
        # 线下充值
        self.http_send(url=url,data=recharge_data,cookies=self.cookies)
        # 查询充值是否成功
        check_url = 'member.php?ctl=uc_money&act=incharge_log'
        result = self.http_send(method='get',url=check_url,cookies=self.cookies)
        return result
if __name__ == '__main__':
    result = Prepay()
    print(result.apiPrepay())