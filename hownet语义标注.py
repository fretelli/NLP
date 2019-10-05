import requests
import json


def hownet_text_sim(input):
    data = {'apiKey': 'obqj67z0', 'input': 'D:/白云山jieba分词与停用词后/白云山2017.txt'}
    url = 'http://yuzhinlp.com/api/getWordAttribute.do'
    html = requests.post(url, data).text
    html = json.loads(html, encoding='utf-8')
    assert isinstance(html, object)
    return html


if __name__ == '__main__':
    print(hownet_text_sim('D:/白云山jieba分词与停用词后/白云山2017.txt'))
