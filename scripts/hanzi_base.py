# 2021/11/14 - 13:53
import json


def merge_base_poly():
    details = []
    with open('polyphone_final.json', 'r', encoding='utf-8') as words:
        contents = json.load(words)
        for single in contents:
            details.append(single)
    print(len(details))

    results = []
    with open('char_base.json', 'r', encoding='utf-8') as common:
        char_json = json.load(common)
        for poly in char_json:
            char = poly['char']
            detail = next((item for item in details if item['char'] == char), False)
            if detail:
                poly['pinyin'] = detail['pinyin']
            else:
                poly['pinyin'] = [poly['pinyin']]
            results.append(poly)

    # results.sort(key=lambda x: x['frequency'])
    print(len(results))
    with open('char_base_poly.json', 'w', encoding='utf-8') as poly:
        poly.write(json.dumps(results, ensure_ascii=False))


def merge_common_base():
    details = []
    with open('char_common.json', 'r', encoding='utf-8') as words:
        contents = json.load(words)
        for single in contents:
            details.append(single)
    # 3500
    print(len(details))

    results = []
    with open('char_base_poly.json', 'r', encoding='utf-8') as common:
        char_json = json.load(common)
        for poly in char_json:
            char = poly['char']
            detail = next((item for item in details if item['char'] == char), False)
            if detail:
                poly['frequency'] = detail['frequency']
            else:
                poly['frequency'] = 3
            results.append(poly)

    # 16146
    print(len(results))
    with open('char_base_common.json', 'w', encoding='utf-8') as poly:
        poly.write(json.dumps(results, ensure_ascii=False))


def sort_char_base():
    results0 = []
    results1 = []
    results2 = []
    results3 = []

    with open('char_base_common.json', 'r', encoding='utf-8') as common:
        char_json = json.load(common)
        for char in char_json:
            freq = char['frequency']
            char['strokes'] = int(char['strokes'])
            if freq == 0:
                results0.append(char)
            elif freq == 1:
                results1.append(char)
            elif freq == 2:
                results2.append(char)
            else:
                results3.append(char)

    results0.sort(key=lambda x: x['strokes'])
    print(len(results0))
    results1.sort(key=lambda x: x['strokes'])
    print(len(results1))
    results2.sort(key=lambda x: x['strokes'])
    print(len(results2))
    results3.sort(key=lambda x: x['strokes'])
    print(len(results3))

    results = []
    results.extend(results0)
    results.extend(results1)
    results.extend(results2)
    results.extend(results3)

    chars = []
    idx = 0
    for result in results:
        idx = idx + 1
        newchar = {'index': idx}
        newchar.update(result)
        chars.append(newchar)

    print(len(results))
    with open('char_base_final.json', 'w', encoding='utf-8') as poly:
        poly.write(json.dumps(chars, ensure_ascii=False))

if __name__ == '__main__':
    # merge_base_poly()
    # merge_common_base()
    sort_char_base()