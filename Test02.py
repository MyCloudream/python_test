# urllib是库，request中该库中的模块，用于发送HTTP请求
import urllib.request
# 引入正则表达式模块
import re
# 网页地址，里面包含众多图片，需要些正则筛选出来
url = "http://www.58pic.com/piccate/5-145-0.html"
# 发送请求
req = urllib.request.urlopen(url)
# 接收相应的内容
res = req.read()
# 将相应的内容转为字符串类型
res = repr(res)
# 正则表达式 前面的一个 r 表示字符串为非转义的原始字符串，让编译器忽略反斜杠，也就是忽略转义字符
# \S匹配任意非空字符 *表示0-n次
regex = r'http://[\S]*.jpg'
# 将正则表达式编译为正则表达式对象，用于提高匹配效率
pattern = re.compile(regex)
# 使用编译好的正则对象调用findall方法，筛选出所有符合正则的数据，结果为list类型
get_image = pattern.findall(res)
# 定义临时变量，用于命名下载的图片
page = 1
for image in get_image:
    # urlretrieve用于将远程数据下载到本地
    urllib.request.urlretrieve(image, "C:/python_test/"+"%s.jpg" % page)
    page += 1
