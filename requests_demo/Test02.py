import requests
from PIL import Image
from io import BytesIO

# 二进制数据
res = requests.get('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1506308627&di=6327a7262a3254b8355557202ae418b8&imgtype=jpg&er=1&src=http%3A%2F%2Fscimg.jb51.net%2Fallimg%2F130104%2F2-130104091152C2.jpg')
img = Image.open(BytesIO(res.content))
img.save("c:/python_test/test.jpg")
