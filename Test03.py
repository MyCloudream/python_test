import urllib.request


# 回调函数定义
def callback(a, b, c):
    '''
    :param a: 已经下载的数据块的个数
    :param b: 数据块的大小，值是8192
    :param c: 远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('%.2f%%' % per)


# 指定下载文件的地址
url = "http://sw.bos.baidu.com/sw-search-sp/software/3756358c42c34/npp_7.5.1_Installer.exe"
# 指定存储的路径和名称
filename = "c:/python_test/notepad++.exe"
# 下载
urllib.request.urlretrieve(url, filename, callback)
