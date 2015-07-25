import json
# -*- coding:utf-8 -*-


keywords = {
    "baidu": {
        1: {
            "words": "哈哈大笑",
            "last_acquired": 0,
            "succ_count": 0,
        },
    },
    "google": {
        1: {
            "words": 'face',
            "last_acquired": 0,
            "succ_count:": 0,
        }
    }
}
baidu = [
    '面无表情',
    '哈哈大笑',
    '气炸了',
]

google = [
    'face', 'infant', 'baby',
    # 'child', 'person', 'girl', 'boy', 'man', 'woman', 'lady', 'gentleman', 'young', 'old',
    # 'infant+face', 'baby+face', 'child+face',
    # 'person+face', 'girl+face', 'beautiful+girl', 'beautiful+girl+face', 'boy+face', 'handsome+boy',
    # 'handsome+boy+face', 'man+face', 'woman+face',
    # 'lady+face', 'gentleman+face', 'young+face', 'young+age', 'young+age+face', 'young+person', 'young+person+face',
    # 'young+man', 'young+man+face',
    # 'young+woman', 'young+woman+face', 'old+face', 'old+age', 'old+age+face', 'old+person', 'old+person+face',
    # 'old+man', 'old+man+face', 'old+woman',
    # 'old+woman+face', 'middle+age', 'middle+age+face', 'middle-age+person', 'middle-age+person+face', 'middle-age+man',
    # 'middle-age+man+face',
    # 'middle-age+woman', 'middle-age+woman+face'
]

i = 0
for kw in google:
    i += 1
    keywords['google'][i] = {}
    keywords['google'][i]['words'] = kw
    keywords['google'][i]['last_acquired'] = 0
    keywords['google'][i]['succ_count'] = 0

i = 0
for kw in baidu:
    i += 1
    keywords['baidu'][i] = {}
    keywords['baidu'][i]['words'] = kw
    keywords['baidu'][i]['last_acquired'] = 0
    keywords['baidu'][i]['succ_count'] = 0

json.dump(keywords, open('keywords.json', 'w'))
