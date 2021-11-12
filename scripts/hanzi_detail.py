# 2021/11/07 - 13:53
import json
import re


def parse_3500():
    """
    解析 3500 常用字详情
    """
    chars = []
    with open('char_common.json', 'r', encoding='utf-8') as common:
        char_json = json.load(common)
        for char in char_json:
            chars.append(char['char'])
    print(chars)
    details = []
    j = 0
    with open('word.json', 'r', encoding='utf-8') as words:
        contents = json.load(words)
        for single in contents:
            word = single['word']
            if word in chars:
                j = j + 1
                print(j)
                details.append(single)

    with open('char_detail.json', "w", encoding="utf-8") as file:
        file.write(json.dumps(details, ensure_ascii=False))


def find_detail():
    '''
    查找出常用字中的汉字详情基本信息
    '''
    results = []
    with open('char_detail.json', "r", encoding="utf-8") as file:
        contents = json.load(file)
        for single in contents:
            word = single['word']
            oldword = single['oldword']
            if word == oldword:
                dic = {'char': word, 'strokes': single['strokes'], 'pinyin': single['pinyin'], 'radicals': single['radicals']}
            else:
                dic = {'char': word, 'traditional': oldword, 'strokes': single['strokes'], 'pinyin': single['pinyin'], 'radicals': single['radicals']}
            results.append(dic)

    with open('char_detail_simple.json', "w", encoding="utf-8") as file:
        file.write(json.dumps(results, ensure_ascii=False))
        

def find_explanation():
    '''
    查找出常用字中的汉字释义
    '''
    results = []
    with open('char_detail.json', "r", encoding="utf-8") as file:
        contents = json.load(file)
        for single in contents:
            desc = single['explanation']
            dic = {'char': single['word'], 'explanation': reduce_explanation(desc)}
            results.append(dic)

    with open('char_explanation.json', "w", encoding="utf-8") as file:
        file.write(json.dumps(results, ensure_ascii=False))


def reduce_explanation(explan):
    return str.strip(explan).replace('⒈', '1.').replace('⒉', '2.').replace('⒊', '3.').replace('⒋', '4.')\
        .replace('⒌', '5.').replace('①', '1.').replace('②', '2.').replace(',', '，').replace(';', '；')


def parse_detail():
    results = []
    with open('char_explanation.json', "r", encoding="utf-8") as file:
        contents = json.load(file)
        for single in contents:
        # for single in contents[0:1]:
            desc = single['explanation']
            lines = str.split(desc, "xxx")
            texts = []
            details = []
            prons = []
            is_title = True
            for line in lines:
                title = find_title(line)
                if len(title) == 1:
                    print('title ' + title)
                else:
                    rows = check_pinyin(line)
                    if len(rows) == 1:
                        if is_pinyin(rows[0]):
                            is_title = False
                            texts = []
                            simple = {'pinyin': str.strip(rows[0]), 'texts': texts}
                            prons.append(simple)
                        else:
                            if is_title:
                                details.append(line2detail(line))
                            else:
                                texts.append(line2detail(line))
                    elif len(rows) > 1:
                        print(rows)
                        is_title = False
                        texts = []
                        texts.append(line2detail(rows[1]))
                        expl = {'pinyin': str.strip(rows[0]), 'texts': texts}
                        prons.append(expl)
                    else:
                        print('--------------')
                        print(rows)

            dic = {'char': str.strip(single['char']), 'details': details, 'pronunciations': prons}
            results.append(dic)

    with open('char_explanations.json', "w", encoding="utf-8") as file:
        file.write(json.dumps(results, ensure_ascii=False))


def find_title(line):
    char = str.strip(line).replace('〈名〉', '').replace('〈动〉', '').replace('〈助〉', '')\
        .replace('〈形〉', '').replace('〈叹〉', '').strip()
    return char


def is_pinyin(word):
    chars = str.strip(word)
    pattern = re.compile(r'[Aa-zZāáǎàōóǒòēéěèīíǐìūúǔùüǖǘǚǜńňǹḿmɡ]+')
    return pattern.match(chars)


def check_pinyin(line):
    chars = str.strip(line)
    lines = []
    pattern = re.compile(r'[Aa-zZāáǎàōóǒòēéěèīíǐìūúǔùüǖǘǚǜńňǹḿmɡ\s]+')
    match = pattern.match(chars, 1, 7)
    if match and match.group():
        splits = pattern.split(chars, 1)
        splits = [i for i in splits if i != '']
        lines.append(match.group())
        if len(splits) > 1:
            lines.append(splits[1])
    else:
        lines.append(chars)
    return lines


def line2detail(detail_line):
    content = str.strip(detail_line).replace('①', '1.').replace('②', '2.').replace('③', '3.')\
        .replace('④','4.').replace('⑤', '5.').replace('⑥', '6.').replace('⑦', '7.')\
        .replace('⑧', '8.').replace('⑨', '9.').replace('⑩', '10.').replace('⒍', '6.')\
        .replace('⒎', '7.').replace('⒏', '8.')
    pattern = re.compile(r'[1-9]+\.')
    match = pattern.search(content)
    if match and match.group():
        splits = pattern.split(content)
        splits = [i for i in splits if i != '']
        if len(splits) > 1 :
            return {'li': splits}
        elif len(splits) == 1:
            ptn = re.compile(r'^[1-9]+\.')
            mth = ptn.match(content)
            if mth and mth.group():
                return {'ol': content}
            else:
                return {'ul': splits[0]}
    return {'ul': content}


def first10():
    results = []
    with open('char_explanations.json', "r", encoding="utf-8") as file:
        contents = json.load(file)
        for single in contents[220:230]:
            results.append(single)

    with open('char_test.json', "w", encoding="utf-8") as file:
        file.write(json.dumps(results, ensure_ascii=False))


if __name__ == '__main__':
    # parse_3500()
    # find_explanation()
    find_detail()
    # parse_detail()
    # first10()
    # line = '啊a 1.助词。用在句末表示感叹的语气。 2.助词。用在句末表示肯定﹑辩解﹑催促﹑嘱咐等语气。 3.助词。用在句末表示疑问的语气。 4.助词。用在句中表示停顿。\n\n 5.助词。用在列举的事项之后。'
    # print(line2detail(line))
