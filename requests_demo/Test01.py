import requests

# 基本使用

'''
res = requests.get('http://www.httpbin.org')
print(res.text)
'''

# 带参数的get请求
'''
res = requests.get('http://www.httpbin.org/get', params={'username': 'cloudream'})
print(res.url)
print(res.text)
'''
# 带参数，带请求头的post请求
'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
res = requests.post('http://www.ucai.cn/index.php?app=fullstack&mod=Public&act=doLogin',
                    data={'account': 'cloudream', 'password': '654321', 'remember': 'undefined'}, headers=None)
print(res.text)
'''
