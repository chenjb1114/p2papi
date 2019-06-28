from libs.Tools import BaseHttp
from libs.base_work import apiLogin

def apiPrepay():
    run = BaseHttp()
    # 线下充值接口
    url = 'member.php?ctl=uc_money&act=incharge_done'
    # 线下充值传参数据
    recharge_data = {
        'check_ol_bl_pay':'on',
        'money':'300',
        'pingzheng':'',
        'memo':'878768',
        'payment':'5',
        'bank_id':'2',
    }
    phpid = apiLogin()
    cookies = {
        'PHPSESSID': phpid
    }
    # 登录
    # pid = apiLogin()
    # cookies = {
    #     'PHPSESSID': pid
    # }
    # 线下充值
    run.http_send(url=url,data=recharge_data,cookies=cookies)
    # 查询充值是否成功
    check_url = 'member.php?ctl=uc_money&act=incharge_log'
    result = run.http_send(method='get',url=check_url,cookies=cookies)
    return result.text
if __name__ == '__main__':
    result = apiPrepay()
    print(result)