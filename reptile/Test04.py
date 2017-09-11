# -*- coding: utf-8 -*-

import time
from urllib import request
from qiniu import Auth, put_file


class UploadDownload:
    def __init__(self, bucket_name, access_key, secret_key):
        self.bucket_name = bucket_name
        self.access_key = access_key
        self.secret_key = secret_key

    # 下载图片
    def download_image(self, url):
        # urlretrieve用于将远程数据下载到本地 time.time()用于获取时间戳
        image_name = str(int(time.time()))
        request.urlretrieve(url, "C:/python_test/" + "%s.jpg" % image_name)
        return "C:/python_test/" + image_name + ".jpg"

    # 上传图片到七牛云存储
    def upload_image(self, save_name, file_path):
        # 构建鉴权对象,需要填写你的 Access Key 和 Secret Key
        q = Auth(self.access_key, self.secret_key)
        # 生成上传 Token，可以指定过期时间等,第一个参数是指上传到哪个bucket，第二个参数值保存到七牛的文件的名称
        token = q.upload_token(self.bucket_name, save_name, 3600)
        # 要上传文件的本地路径，第二个参数是保存到七牛的文件的名称，第三个参数为要上传的文件的完整路径
        put_file(token, save_name, file_path)


def main():
    # 创建UploadDownload对象，包含3个属性
    ud = UploadDownload('reptile', '', '')
    # 调用ud对象的下载图片方法
    image_name = ud.download_image('https://cdn.pixabay.com/photo/2015/06/22/08/37/children-817365_960_720.jpg')
    # 对下载的图片上传
    ud.upload_image(image_name.split('/')[-1], image_name)


if __name__ == '__main__':
    main()
