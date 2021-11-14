# 2021/11/10 - 8:53
import json
import re


def parse_pinyin():
    """
    基础数据结构化，TXT 转为 JSON
    最终发现，此数据可靠性低
    废弃
    """
    results = []
    idx = 0
    for content in open('pinyin.txt', "r", encoding="utf-8"):
        idx = idx + 1
        if idx > 2:
            word = content[8:]
            splits = word.split('#')
            print(splits)
            pinyins = splits[0].split(',')
            pinyins = [s.strip() for s in pinyins]
            result = {'char': splits[1].strip(), 'pinyin': pinyins}
            results.append(result)

    with open('deprecated_pinyin.json', "w", encoding="utf-8") as file:
        file.write(json.dumps(results, ensure_ascii=False))


def parse_poly_3000():
    results = []
    for content in open('tmp.txt', "r", encoding="utf-8"):
        pattern = re.compile("(?<=\\()(.*)(?=\\))")
        findall = pattern.findall(content)
        word = content[0]
        hanzi = re.compile(r'[\u4e00-\u9fa5]')
        match = hanzi.match(word)
        if match and match.group():
            splits = str.split(findall[0], "/")
            pinyins = [s.strip() for s in splits]
            result = {'char': word, 'pinyin': pinyins}
            results.append(result)
    print(len(results))
    with open('poly_origin_all.json', "w", encoding="utf-8") as file:
        file.write(json.dumps(results, ensure_ascii=False))


def parse_poly_txt():
    """
    处理多音字 txt 文件，得到 363
    """
    results = []
    for content in open('poly.txt', "r", encoding="utf-8"):
        pattern = re.compile("(?<=【)([Aa-zZāáǎàōóǒòēéěèīíǐìūúǔùüǖǘǚǜńňǹḿmɡ]+)(?=】)")
        findall = pattern.findall(content)
        word = content[0]
        pinyins = [s.strip() for s in findall]
        result = {'char': word, 'pinyin': pinyins}
        results.append(result)

    print(len(results))
    with open('poly_origin.json', "w", encoding="utf-8") as file:
        file.write(json.dumps(results, ensure_ascii=False))


def parse_poly():
    '''
    解析出多音字，363组
    :return:
    '''
    chars1 = []
    with open('char_common.json', 'r', encoding='utf-8') as common:
        char_json = json.load(common)
        for char1 in char_json:
            chars1.append(char1['char'])
    print(len(chars1))
    chars2 = []
    with open('char_secondary.json', 'r', encoding='utf-8') as secondary:
        char_sec = json.load(secondary)
        for char2 in char_sec:
            chars2.append(char2['char'])

    result = []
    with open('poly_origin.json', 'r', encoding='utf-8') as file:
        contents = json.load(file)
        print(len(contents))
        for content in contents:
            char = content['char']
            pinyin = content['pinyin']
            if len(pinyin) > 1:
                if char in chars1:
                    if char in chars2:
                        content['frequency'] = 2
                    else:
                        content['frequency'] = 1
                else:
                    content['frequency'] = 3
                result.append(content)
            else:
                print(content)

    result.sort(key=lambda x: x['frequency'])
    print(len(result))
    with open('polyphone.json', 'w', encoding='utf-8') as poly:
        poly.write(json.dumps(result, ensure_ascii=False))


def merge_poly_all_char_common():
    chars1 = []
    with open('char_common.json', 'r', encoding='utf-8') as common:
        char_json = json.load(common)
        for char1 in char_json:
            chars1.append(char1['char'])
    print(len(chars1))
    chars2 = []
    with open('char_secondary.json', 'r', encoding='utf-8') as secondary:
        char_sec = json.load(secondary)
        for char2 in char_sec:
            chars2.append(char2['char'])

    result = []
    with open('poly_origin_all.json', 'r', encoding='utf-8') as file:
        contents = json.load(file)
        print(len(contents))
        for content in contents:
            char = content['char']
            pinyin = content['pinyin']
            if len(pinyin) > 1:
                if char in chars1:
                    if char in chars2:
                        content['frequency'] = 2
                    else:
                        content['frequency'] = 1
                else:
                    content['frequency'] = 3
                result.append(content)
            else:
                print(content)

    result.sort(key=lambda x: x['frequency'])
    print(len(result))
    with open('polyphone_all.json', 'w', encoding='utf-8') as poly:
        poly.write(json.dumps(result, ensure_ascii=False))


def find_poly_char():
    chars1 = []
    with open('polyphone_all.json', 'r', encoding='utf-8') as common:
        char_json = json.load(common)
        for char1 in char_json:
            chars1.append(char1['char'])
    print(len(chars1))

    results = []
    with open('polyphone.json', 'r', encoding='utf-8') as file:
        contents = json.load(file)
        print(len(contents))
        for content in contents:
            char = content['char']
            if char not in chars1:
                results.append(content)

    print(len(results))
    with open('polyphone_diff.json', 'w', encoding='utf-8') as poly:
        poly.write(json.dumps(results, ensure_ascii=False))


def add_word():
    details = []
    with open('polyphone_full.json', 'r', encoding='utf-8') as words:
        contents = json.load(words)
        for single in contents:
            details.append(single)
    print(len(details))
    tmp = []
    with open('polyphone_diff.json', 'r', encoding='utf-8') as polyfile:
        polys = json.load(polyfile)
        for poly in polys:
            tmp.append(poly)

    print(len(tmp))
    details.extend(tmp)
    print(len(details))

    details.sort(key=lambda x: x['frequency'])

    with open('polyphone_all.json', "w", encoding="utf-8") as file:
        file.write(json.dumps(details, ensure_ascii=False))


def classify_frequency():
    chars = []
    for content in open('tmp.txt', "r", encoding="utf-8"):
        splits = str.split(content, ' ')
        chars = splits
    print(len(chars))

    results = []
    idx = 0
    with open('polyphone_all.json', 'r', encoding='utf-8') as common:
        char_json = json.load(common)
        for item in char_json:
            char = item['char']
            idx = idx + 1
            new_item = {"index": idx}
            if char in chars:
                item['frequency'] = 0
            new_item.update(item)
            results.append(new_item)

    results.sort(key=lambda x: x['frequency'])
    print(len(results))
    with open('polyphone.json', 'w', encoding='utf-8') as poly:
        poly.write(json.dumps(results, ensure_ascii=False))


def classify_stroke():
    details = []
    with open('char_base.json', 'r', encoding='utf-8') as words:
        contents = json.load(words)
        for single in contents:
            details.append(single)
    print(len(details))

    results = []
    with open('polyphone.json', 'r', encoding='utf-8') as common:
        char_json = json.load(common)
        for poly in char_json:
            char = poly['char']
            detail = next((item for item in details if item['char'] == char), False)
            if detail:
                poly['strokes'] = int(detail['strokes'])
                results.append(poly)
            else:
                print(char)

    results.sort(key=lambda x: x['frequency'])
    print(len(results))
    with open('polyphone_final.json', 'w', encoding='utf-8') as poly:
        poly.write(json.dumps(results, ensure_ascii=False))


if __name__ == '__main__':
    # parse_poly_txt()
    # parse_poly_3000()
    # parse_poly()
    # find_poly_char()
    # add_word()
    # merge_poly_all_char_common()
    # classify_frequency()
    classify_stroke()