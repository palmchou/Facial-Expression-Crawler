import json
# -*- coding:utf-8 -*-

# Emotion classification:
# happiness sadness surprise anger disgust fear neutral



keywords = {
    "baidu": {
        1: {
            "classification": "smile",
            "words": "哈哈大笑",
            "last_acquired": 0,
            "succ_count": 0,
        },
    },
    "google": {
        1: {
            "classification": "sadness",
            "words": 'face',
            "last_acquired": 0,
            "succ_count:": 0,
        }
    }
}
baidu = {
    "happiness": [
        '笑','笑容','微笑', '大笑','欢笑','坏笑','哄笑','狂笑',
    ],
    "sadness": [
        '哭','大哭','啜泣','呜咽','低泣','嚎啕大哭',
    ],
    "surprise": [
        '惊讶','震惊','惊愕','大吃一惊','目瞪口呆','张口结舌',
    ],
    "anger": [
        '生气','愤怒','恼火','狂怒','瞪眼','怒视','皱眉','生闷气','怒气冲冲','咬牙切齿',
    ],
    "disgust": [
        '厌恶',
    ],
    "fear": [
        '恐惧','惧怕','畏惧',
    ],
    "neutral": [
        '面无表情'
    ]
}

google = {
    "happiness": [
        'smile', 'beam', 'horselaugh', 'grin', 'chuckle', 'giggle', 'smirk', 'simper', 'cachinnate', 'laugh', 'snicker', 'chortle', 'roar', 'guffaw',
    ],
    "sadness": [
        'cry', 'weep', 'sob', 'whimper', 'mewl', 'blubber', 'lament', 'yowl', 'whine', 'wail', 'snivel',
    ],
    "surprise": [
        'surprise', 'amaze', 'astounded', 'gape',
    ],
    "anger": [
        'cry', 'weep', 'sob', 'whimper', 'mewl', 'blubber', 'lament', 'yowl', 'whine', 'wail', 'snivel',
    ],
    "disgust": [
        'disgust',
    ],
    "fear": [
        'fear',
    ],
    "neutral": [
        'expressionless','poker+faced'
    ]
}

# i = 0
# for kw in google:
#     i += 1
#     keywords['google'][i] = {}
#     keywords['google'][i]['words'] = kw
#     keywords['google'][i]['last_acquired'] = 0
#     keywords['google'][i]['succ_count'] = 0

i = 0
for (type, dict) in google.items():
    for kw in dict:
        i += 1
        keywords['google'][i] = {}
        keywords['google'][i]['words'] = kw
        keywords['google'][i]['last_acquired'] = 0
        keywords['google'][i]['succ_count'] = 0
        keywords['google'][i]['classification'] = type
for (type, dict) in baidu.items():
    for kw in dict:
        i += 1
        keywords['google'][i] = {}
        keywords['google'][i]['words'] = kw
        keywords['google'][i]['last_acquired'] = 0
        keywords['google'][i]['succ_count'] = 0
        keywords['google'][i]['classification'] = type

#
# i = 0
# for kw in baidu:
#     i += 1
#     keywords['baidu'][i] = {}
#     keywords['baidu'][i]['words'] = kw
#     keywords['baidu'][i]['last_acquired'] = 0
#     keywords['baidu'][i]['succ_count'] = 0
#
i = 0
for (type, dict) in baidu.items():
    for kw in dict:
        i += 1
        keywords['baidu'][i] = {}
        keywords['baidu'][i]['words'] = kw
        keywords['baidu'][i]['last_acquired'] = 0
        keywords['baidu'][i]['succ_count'] = 0
        keywords['baidu'][i]['classification'] = type


json.dump(keywords, open('keywords.json', 'w'))