# 导入模块
from urllib import request
# 指定要下载的图片的地址
url = "http://pic.qiantucdn.com/images/banner/59ad4e6c86b91.jpg"
# 发送请求
request = request.urlopen(url)
# 获取返回结果
response = request.read()
# 创建一个图片文件，名称和图片原名称一致
f = open("C:/python_test/"+url.split("/")[-1],"wb")
# 写入数据
f.write(response)
# 关闭文件
f.close()