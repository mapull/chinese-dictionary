# 2021/11/07 - 13:53
import json
import re


def add_word():
    details = []
    with open('word_tmp.json', 'r', encoding='utf-8') as words:
        contents = json.load(words)
        for single in contents:
            details.append(single)

        tmp1 = {
            "word": "囱",
            "oldword": "囱",
            "strokes": "7",
            "pinyin": "cōng",
            "radicals": "口",
            "explanation": "囱〈叹〉\n\n 〔烟囱〕炉灶出烟的通路。",
            "more": "囱 cōng 灶突。今称烟囱〖chimney〗\n 囱,通孔也,灶突也。 -- 《玉篇》"
        }
        details.append(tmp1)
        tmp2 = {
            "word": "啰",
            "oldword": "囉",
            "strokes": "11",
            "pinyin": "luō",
            "radicals": "口",
            "explanation": "啰luō 〔啰唆〕1.说话絮絮叨叨；2.办事不痛快，使人感觉麻烦。均亦作“啰嗦”。\n\n 啰luó 〔啰唣〕吵闹。 \n\n 啰luo 助词，作用大致和”了“一样：这样就好啰！",
            "more": "啰 ga、a 部首 口 部首笔画 03 总笔画 11  啰嗦 luōsuo 1.言语繁复 啰嗦的社论 2.琐碎;麻烦 这个工作真啰嗦。\n\n 啰唣 luózào 见”罗唣“(luózào) \n\n 啰 luo 【助】 放在句末,表示一种情况或感情\n\n 用在句末表示情况的变化。  放 -- 炮 -- 啰!他有了新的想法啰! \n\n 表示赞叹。 大家都满怀信心啰! 表示祈使。 \n\n 请你们放心啰! 用在句末,表示肯定。 \n\n 他准能办到啰。"
        }
        details.append(tmp2)

        tmp3 = {
            "word": "屎",
            "oldword": "宩",
            "strokes": "9",
            "pinyin": "shǐ",
            "radicals": "尸",
            "explanation": "屎shǐ \n\n 大便，粪。\n\n 眼、耳所分泌的东西：眼屎。耳屎。\n\n 嘲笑低能的：屎棋。屎诗。",
            "more": "屎 shǐ 屎滚尿流shǐgǔn-niàoliú \n 犹“屁滚尿流”。形容惊恐的样子。\n\n  屎壳郎 shǐkelàng 蜣螂。\n\n  屎盆子 shǐpénzi 比喻恶名或坏事。自己做的丢人事,哪能把屎盆子扣别人头上。屎桶shǐtǒng [方言]∶比喻孤傲,无人理睬。他以为自己是什么?屎桶,还两眼向天不看人呢?"
        }
        details.append(tmp3)

        tmp4 = {
            "word": "铝",
            "oldword": "鋁",
            "strokes": "11",
            "pinyin": "lǚ",
            "radicals": "钅",
            "explanation": "铝 \n\n 一种金属元素，质地坚韧而轻，有延展性，容易导电。可作飞机、车辆、船、舶、火箭的结构材料。纯铝可做超高电压的电缆。\n\n 铝lǚ 带蓝色的银白色三价金属元素,延展性好,有韧性并能发出〖响亮〗声音,以其轻、良好的导电和导热性能、高反射性和耐氧化而著称,是地壳中含量最丰富的金属,在7%以上〖aluminium〗 -- 元素符号Al。",
            "more": "铝 lǚ 铝合金lǚhéjīn \n 铝和较少量其他金属如铜、镁或锰组成的合金 。\n\n  铝矿 lǚkuàng  从中可以经济地提炼铝的一种天然矿石。"
        }
        details.append(tmp4)

    with open('word.json', "w", encoding="utf-8") as file:
        file.write(json.dumps(details, ensure_ascii=False))


def parse_3500():
    """
    解析 3500 常用字详情
    """
    chars = []
    with open('char_common.json', 'r', encoding='utf-8') as common:
        char_json = json.load(common)
        for char in char_json:
            chars.append(char['char'])
    print(len(chars))
    details = []
    with open('word.json', 'r', encoding='utf-8') as words:
        contents = json.load(words)
        print(len(contents))
        for single in contents:
            word = single['word']
            if word in chars:
                details.append(single)
    print(len(details))
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
    print(len(results))
    with open('char_detail_tmp.json', "w", encoding="utf-8") as file:
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
    # add_word()
    # parse_3500()
    find_detail()
    # find_explanation()
    # parse_detail()
    # first10()
    # line = '啊a 1.助词。用在句末表示感叹的语气。 2.助词。用在句末表示肯定﹑辩解﹑催促﹑嘱咐等语气。 3.助词。用在句末表示疑问的语气。 4.助词。用在句中表示停顿。\n\n 5.助词。用在列举的事项之后。'
    # print(line2detail(line))
