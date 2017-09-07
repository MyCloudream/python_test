from urllib import request, parse
import json


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
    ('questionCount', '10'),
    ('tagIds', '570'),
    ('t', '02436CC60E649584D5C4BBF57709E5CA'),
    ('fm', 'android_app_2.21.3.3091'),
    ('source', '1')
])


def write_text(path, text, mode='a'):
    with open(path, mode=mode, encoding="utf-8") as f:
        f.write(text)
        f.write("<br>")


url_get_questions = "http://m.nowcoder.com/test/get-all-question?t=02436CC60E649584D5C4BBF57709E5CA&fm=android_app_2.21.3.3091&tid=10679830"
all_questions = get_json_data(url_get_questions)['data']['allQuestion']
n = 1
for item_question in all_questions:
    question = item_question['question']
    print(question['content'])
    write_text("C://python_test/a.html", str(n)+". "+question['content'], 'a')
    answer = question['answer']
    answer_option = ''
    index = 0
    for item_answer in answer:
        answer_content = item_answer['content']
        print(answer_content)
        answer_index_list = ['A', 'B', 'C', 'D']
        write_text("C://python_test/a.html", answer_index_list[index]+". "+answer_content, 'a')
        answer_type = item_answer['type']
        if answer_type == 1:
            answer_option += answer_index_list[index]
        index += 1
    print(answer_option)
    write_text("C://python_test/b.html", '', 'a')
    write_text("C://python_test/b.html", str(n)+"."+'答案: ' + answer_option, 'a')
    write_text("C://python_test/b.html", '', 'a')
    n += 1
