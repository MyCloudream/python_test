from urllib import request, parse
import json


def post_json_data(url, request_body):
    req = request.Request(url)
    req.add_header('OS', 'Android')
    req.add_header('VERSION', '82')
    req.add_header('CHANNEL', '360')
    req.add_header('User-Agent', 'nowcoder android 2.21.3.3091')
    with request.urlopen(req, data=request_body.encode('utf-8')) as f:
        if f.status == 200:
            result_json = json.loads(f.read())
            return result_json


def get_json_data(url):
    req = request.Request(url)
    req.add_header('OS', 'Android')
    req.add_header('VERSION', '82')
    req.add_header('CHANNEL', '360')
    req.add_header('User-Agent', 'nowcoder android 2.21.3.3091')
    with request.urlopen(req) as f:
        if f.status == 200:
            result_json = json.loads(f.read())
            return result_json


data_make_paper = parse.urlencode([
    ('questionCount', '30'),
    ('tagIds', '570'),
    ('t', '02436CC60E649584D5C4BBF57709E5CA'),
    ('fm', 'android_app_2.21.3.3091'),
    ('source', '1')
])

result = post_json_data('http://m.nowcoder.com/itest/request-make-paper', data_make_paper)
print(result['data'])

url_get_questions = "http://m.nowcoder.com/test/get-all-question?t=02436CC60E649584D5C4BBF57709E5CA&fm=android_app_2.21.3.3091&tid=" + \
                    str(result['data'])
print(get_json_data(url_get_questions))
