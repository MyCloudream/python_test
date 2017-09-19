from urllib import request, parse
import json


def post_json_data(url, request_body):
    req = request.Request(url)
    # 根据需要设置请求头，比如模拟浏览器请求设置UA、一些身份权限认证字段等都会放到header里
    req.add_header('OS', 'Android')
    req.add_header('VERSION', '82')
    req.add_header('CHANNEL', '360')
    req.add_header('User-Agent', 'nowcoder android 2.21.3.3091')
    # post请求，添加request body即可
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


def write_text(path, text, mode='a'):
    with open(path, mode=mode, encoding="utf-8") as f:
        f.write(text)
        f.write("<br>")


result = post_json_data('http://m.nowcoder.com/itest/request-make-paper', data_make_paper)
url_get_questions = "http://m.nowcoder.com/test/get-all-question" + \
                    "?t=02436CC60E649584D5C4BBF57709E5CA&fm=android_app_2.21.3.3091&tid=" + \
                    str(result['data'])
all_questions = get_json_data(url_get_questions)['data']['allQuestion']
# 题号信息，由于获取的题目没有编号
n = 1
# 提取出来方便修改，如果有明确的题目数量，可以嵌套一层循环来循环获取n套题。这里我们获取1套题作为演示
# 之所以写入到html文件，是因为读取的题目中含有html的格式信息
questions_name = "第11套.html"
questions_answer_name = "第11套答案.html"
for item_question in all_questions:
    # 获取题干信息
    question = item_question['question']
    question_type = ['(单选题)', '(不定项选择题)']
    # 写入题目信息
    write_text("C://python_test/"+questions_name, str(n)+". "+question_type[question['type']-1]+question['content'], 'a')
    answer = question['answer']
    answer_option = ''
    index = 0
    for item_answer in answer:
        # 获取选项信息
        answer_content = item_answer['content']
        answer_index_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        # 写入选项信息，加入ABCD等选项编号
        write_text("C://python_test/"+questions_name, answer_index_list[index]+". "+answer_content, 'a')
        # 获取type字段的值，为1表示该选项为正确答案
        answer_type = item_answer['type']
        if answer_type == 1:
            # 获取正确答案
            answer_option += answer_index_list[index]
        index += 1
    # 每题之间留空行
    write_text("C://python_test/"+questions_name, '', 'a')
    # 写入答案到另外一个文件中
    write_text("C://python_test/"+questions_answer_name, str(n)+"."+'答案: ' + answer_option, 'a')
    # 答案之间留空行
    write_text("C://python_test/"+questions_answer_name, '', 'a')
    # 编号自增
    n += 1
