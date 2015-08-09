import json
# -*- coding:utf-8 -*-

# Emotion classification:
# happiness sadness surprise anger disgust fear neutral



keywords = {
    "baidu": {
        # 1: {
        #     "classification": "smile",
        #     "words": "哈哈大笑",
        #     "last_acquired": 0,
        #     "succ_count": 0,
        # },
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
    # "happiness": [
    #     # '笑','笑容','微笑', '大笑','欢笑','坏笑','哄笑','狂笑',
    #     #
    #     '爱笑的女孩', '爱笑的男孩', '爱笑的小孩', '爱笑的叔叔', '爱笑的阿姨', '爱笑的奶奶', '爱笑的爷爷',
    #     '空姐微笑', '坏笑 少年'
    # ],
    # "sadness": [
    #     # '哭','大哭','啜泣','呜咽','低泣','嚎啕大哭',
    #     '哭泣',
    #     '爱哭的小孩', '爱哭的女孩', '爱哭的男孩',
    #     '大哭的小孩', '大哭的女孩', '大哭的男孩', '大哭的少女', '大哭的少年', '大哭的婴儿'
    #     '啜泣的女孩', '啜泣的男孩', '呜咽的女孩', '呜咽的男孩', '哭泣的女孩', '哭泣的男孩',
    #     '爷爷流泪', '奶奶流泪', '妈妈流泪', '爸爸流泪', '幸福的泪水',
    # ],
    # "surprise": [
    #     # '惊讶', '震惊', '惊愕', '大吃一惊', '目瞪口呆', '张口结舌',
    #     '惊讶的样子', '惊讶的表情', '震惊的样子', '震惊的表情', '大吃一惊的样子', '大吃一惊的表情',
    #     '目瞪口呆的样子', '目瞪口呆的表情',
    #     '吃惊的小孩', '吃惊的女孩', '吃惊的男孩', '吃惊的少女', '吃惊的少年', '吃惊的叔叔',
    #     '弟弟很惊讶', '妹妹很惊讶', '爸爸很惊讶', '妈妈很惊讶', '爷爷很惊讶', '奶奶很惊讶',
    #     '弟弟震惊', '妹妹震惊', '女孩震惊', '男孩震惊', '父亲震惊', '母亲震惊',
    #     '目瞪口呆的小孩', '目瞪口呆的女孩', '目瞪口呆的男孩', '目瞪口呆的少女', '目瞪口呆的少年',
    # ],
    # "anger": [
    #     # '生气', '愤怒', '恼火', '狂怒', '瞪眼', '怒视', '皱眉', '生闷气', '怒气冲冲', '咬牙切齿',
    #     '发怒', '发火'
    #     '生气的样子', '生气的表情', '愤怒的样子', '愤怒的表情', '恼火的样子', '恼火的表情', '瞪眼的样子',
    #     '瞪眼的表情', '怒视的样子', '怒视的表情', '生闷气的样子', '生闷气的表情', '怒气冲冲的样子', '怒气冲冲的表情',
    #     '咬牙切齿的样子', '咬牙切齿的表情', '发怒的样子', '发怒的表情', '发火的样子', '发火的表情',
    #     '生气的小孩', '生气的婴儿', '生气的儿子', '生气的女儿', '生气的女孩', '生气的男孩', '生气的姑娘', '生气的小伙子',
    #     '爸爸生气', '妈妈生气', '爷爷生气', '奶奶生气', '生气的老人', '生气的老大爷', '生气的老奶奶', '生气的大妈', '生气的老爷爷',
    #     '愤怒的婴儿', '恼火的婴儿', '恼火的女孩', '恼火的男孩', '愤怒的女孩', '愤怒的男孩', '愤怒的姑娘', '愤怒的小伙子',
    #     '愤怒的年轻人', '愤怒的爸爸', '愤怒的妈妈', '愤怒的中年', '愤怒的老人', '愤怒的老奶奶', '愤怒的老爷爷',
    #     '皱眉头的妈妈', '皱眉头的爸爸', '皱眉头的爷爷', '皱眉头的奶奶', '爸爸发怒', '妈妈发怒', '爸爸发火', '妈妈发火',
    # ],
    # "disgust": [
    #     # '厌恶',
    #     '厌恶的样子', '厌恶的表情', '不屑一顾',
    #     '厌烦', '厌烦的样子', '厌烦的表情', '不屑一顾样子', '不屑一顾的表情',
    #     '讨厌', '讨厌的样子', '讨厌的表情',
    #     '不耐烦', '不耐烦的样子', '不耐烦的表情',
    #     '不耐烦的婴儿', '不耐烦的小孩', '不耐烦的女孩', '不耐烦的男孩', '不耐烦的小伙子', '不耐烦的姑娘',
    #     '厌恶的神态', '讨厌的神态', '不耐烦的神态',
    # ],
    # "fear": [
    #     # '恐惧', '惧怕', '畏惧',
    #     '害怕', '受到惊吓', '惊恐',
    #     '恐惧的样子', '恐惧的表情', '惧怕的样子', '惧怕的表情', '畏惧的样子', '畏惧的表情',
    #     '受到惊吓的样子', '受到惊吓的表情', '惊恐的样子', '惊恐的表情',
    #     '受到惊吓的小孩', '受到惊吓的女孩', '受到惊吓的男孩', '受到惊吓的姑娘', '受到惊吓的小伙子',
    #     '惊恐的小孩', '惊恐的女孩', '惊恐的男孩', '惊恐的少女', '惊恐的少年',
    # ],
    # "neutral": [
    #     '面无表情',
    #     '面无表情的样子',
    #     '证件照',
    # ]
}

google = {
    "happiness": [
        # 'smile', 'beam', 'horselaugh', 'grin', 'chuckle', 'giggle', 'smirk', 'simper', 'cachinnate', 'laugh', 'snicker',
        # 'chortle', 'roar', 'guffaw',
        'smile facial expression', 'smile facial man', 'smile facial woman', 'smile facial girl', 'smile facial boy',
        'smile facial old', 'smile by facial',
    ],
    "sadness": [
        # 'cry', 'weep', 'sob', 'whimper', 'mewl', 'blubber', 'lament', 'yowl', 'whine', 'wail', 'snivel',
        'cry facial expression', 'cry facial man', 'cry facial woman', 'cry facial boy', 'cry facial girl',
        'cry facial baby', 'cry facial old', 'cry by facial',
        'sad face', 'sad facial expression', 'sad facial man', 'sad facial woman', 'sad facial girl', 'sad facial boy',
        'sad facial baby', 'sad facial old', 'sad by facial',
        'upset', 'upset face', 'upset facial expression', 'upset facial man', 'upset facial woman', 'upset facial girl',
        'upset facial boy', 'upset facial baby', 'upset facial old', 'upset by facial',
    ],
    "surprise": [
        # 'surprise', 'amaze', 'astounded', 'gape',
        'surprising face', 'surprising facial expression', 'surprising facial man', 'surprising facial woman',
        'surprising facial girl', 'surprising facial boy', 'surprising facial baby', 'surprising facial old',
        'surprising by facial', 'surprised face', 'surprised facial expression', 'surprised facial man',
        'surprised facial woman', 'surprised facial girl', 'surprised facial boy', 'surprised facial baby',
        'surprised facial old', 'surprised by facial',
    ],
    "anger": [
        'anger', 'rage', 'glare', 'glower', 'scowl', 'sulky', 'snarl', 'gnash',
        'angry face', 'angry facial expression', 'angry facial man', 'angry facial woman', 'angry facial girl',
        'angry facial boy', 'angry facial baby', 'angry facial old', 'angry by facial',
        'anger facial expression', 'anger facial man', 'anger facial woman', 'anger facial boy', 'anger facial girl',
        'anger facial baby', 'anger facial old', 'anger by facial',
        'rage face', 'rage facial expression', 'rage facial man', 'rage facial woman', 'rage facial boy',
        'rage facial girl', 'rage facial baby', 'rage facial old', 'rage by facial',
    ],
    "disgust": [
        # 'disgust',
        'disgusted facial expression', 'disgusted facial man', 'disgusted face man', 'disgusted facial woman',
        'disgusted face woman', 'disgusted facial boy', 'disgusted facial girl', 'disgusted face boy',
        'disgusted face girl', 'disgusted facial baby', 'disgusted face baby', 'disgusted face old',
        'disgusted facial old', 'disgusted by facial',
    ],
    "fear": [
        # 'fear',
        'fear facial expression', 'feared face', 'feared facial expression', 'feared facial man', 'feared facial woman',
        'feared facial girl', 'feared facial boy', 'feared facial baby', 'feared facial old', 'feared by facial',
    ],
    "neutral": [
        'expressionless face', 'expressionless facial', 'expressionless facial man', 'expressionless facial woman',
        'expressionless facial girl', 'expressionless facial boy', 'expressionless facial baby',
        'expressionless facial old', 'expressionless by facial',
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
