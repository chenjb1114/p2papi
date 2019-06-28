import requests
# 登录接口
login_url = 'http://localhost/index.php?ctl=user&act=dologin&fhash=inIRwtRtTAHUvoFmjcpjXdHBNAIQXictVptkoWuXScmCmBxhnu'
# 登录接口参数
login_data  = {
    'email':'13587652131',
    'user_pwd':'U1BIVWp0dXlqYUFkdVpvU2hpYWdBZlBJZHlQUEtMRE1KcHZ0VmlsQUhtYnNrZXdMREElMjV1NjVCOSUyNXU3RUY0amsxNDcyNTglMjV1OEY2RiUyNXU0RUY2',
    'ajax':'1',
}
result = requests.post(url=login_url,data=login_data)
data = result.json()
if result.status_code == 200 and data.get('info') == '成功登录':
    print('测试成功')