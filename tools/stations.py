import re
import requests
from pprint import pprint

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9025'
response = requests.get(url, verify=False)
stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
print(dict(stations))

# 反转dict
dict_res = dict(stations)
dict_res = dict(zip(dict_res.values(), dict_res.keys()))
print(dict_res)