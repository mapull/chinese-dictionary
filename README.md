# 汉语拼音辞典

本词典主要收录了常用字基本信息，多音字，汉字基本解释，常用词汇、常用成语读音。

## 缘起

中华传统文化，源远流长，博大精深！从古至今，上下五千年，在这历史的长河中先辈们创造出了无数的历史奇迹。
在中国两千多年的漫长帝制社会里，汉字一直是我们中华民族文化传承的重要工具。
从甲骨文到秦始皇统一文字，再到近代简化字，汉字一直在经历演变过程。
汉字总数超过8万，但常用字仅2500个，次常用字1000多个，共3500字。
对于不太常见的汉字，我们通常会使用字典、词典的方式来查询。

**汉语拼音辞典** 就属于一个便于用户查询汉字拼音与笔画的电子词典工具。

## 字库

字库的准确性和完整性对于 辞典 工具来说至关重要。本词典收集了如下字、词库：

```text
|---- chinese-dictionary
|----|---- data     数据
|----|----|---- character
|----|----|----|---- char_base.json             总收录汉字 16146 拼音与笔画
|----|----|----|---- char_base_detail.json      总收录汉字 16146 解释
|----|----|----|---- char_common.json           常用字 3500 仅汉字
|----|----|----|---- char_common_base.json      常用字 3500 拼音与笔画
|----|----|----|---- char_common_detail.json    常用字 3500 解释
|----|----|----|---- polyphone.json             多音字 1756
|----|---- scripts    脚本
```

### 数据格式

#### 为何数据是 JSON 格式？

JSON 格式可以方便快捷地转为各种编程语言内部可使用的结构。

此外某些工具支持将 JSON 文件导入后直接结构化。

#### char_base.json 基础汉字

```json
[
  {"index": 1, "char": "一", "strokes": 1, "pinyin": ["yī"], "radicals": "一", "frequency": 0}, 
  {"index": 2770, "char": "咧", "strokes": 9, "pinyin": ["liě", "liē", "lié", "lie"], "radicals": "口", "frequency": 2},
  {"index": 7467, "char": "砭", "strokes": 9, "pinyin": ["biān"], "radicals": "石", "frequency": 3}
]
```

- `index` 表示从 1 开始的自然增长序列，默认按照汉字笔画数排序。
- `char` 表示一个汉字。
- `strokes` 汉字的笔画数。
- `pinyin` 汉字的读音列表。
- `radicals` 汉字的读音偏旁部首。
- `frequency` 表示使用频率，0 为最常用，1 为较常用，2 为次常用，3 为生僻字。
- `traditional` 表示繁体字写法。

> 常用字（3500） = 最常用字 0（500）+ 较常用字 1（2000）+ 次常用字 2（1500） 

#### char_common.json 常用字

```json
[
  {"id": 4, "char": "十", "frequency": 0},
  {"id": 278, "char": "乐", "frequency": 1},
  {"id": 3405, "char": "瞪", "frequency": 2}
]
```

- `id` 表示从 1 开始的自然增长序列，默认按照汉字笔画数排序。
- `char` 表示一个汉字。
- `frequency` 表示使用频率，0 为最常用，1 为较常用，2 为次常用。


#### char_common_base.json 常用字


```json
[
  {"index": 1, "char": "一", "strokes": 1, "pinyin": ["yī"], "radicals": "一", "frequency": 0},
  {"index": 16, "char": "大", "strokes": 3, "pinyin": ["dà", "dài", "tài"], "radicals": "大", "frequency": 0}
]
```

#### char_common_detail.json 常用字

```json
[
    {
      "char": "为",
      "explanations": [
        {
          "contents": [
            "(爲的本义是母猴。象形。按字，从爪，古文下象两母猴相对形)",
            "假借为伪”。做，作，干，搞",
            "我生之初，尚无为。--《诗·王风·兔爰》",
            "子为不知，我将不墜。--《左传·定公十二年》",
            "为善者，非善也，故善无以为也。--《管子·枢言》",
            "变化则为生，为生则乱矣。--《管子·心术上》",
            "为，施也。又，成也。--《广雅》",
            "有客自云能，帝使为之。--《世说新语·巧艺》",
            "为之难。--《论语》。皇疏犹行也。”",
            "可以为师。--《论语》",
            "人之为学。--清·彭端淑《为学一首示子侄》",
            "推为长。--清·徐珂《清稗类钞·战"
          ]
        }
      ],
      "pronunciations": [
        {
          "pinyin": "wéi",
          "explanations": [
            {
              "details": [
                "1.做，干事在人～。敢作敢～。",
                "2.有能力，有贡献，做出成绩年轻有～。大有作～。",
                "3.看成，当作认～。以～。不足～凭。霓～衣兮风～马。",
                "4.充当，担任，治理能者～师。她～校长已三年。善～国事。",
                "5.成，变成变荒坡～花果山。",
                "6.是十两～一斤。",
                "7.被～人所耻。",
                "8.助词。〈表〉疑问、程度、范围、加强语气等何乐不～？大～不幸。广～流传。极～紧要。"
              ]
            }
          ]
        },
        {
          "pinyin": "wèi",
          "explanations": [
            {
              "details": [
                "1.给，替～国争光。～人民服务。",
                "2.〈表〉目的～了治病救人。",
                "3.向，对且～众人言。不足～外人道。",
                "4.帮助，卫护～人作嫁（〈喻〉没有自己的好处，白给别人操劳）。～虎作伥（〈喻〉做坏人的帮凶）。"
              ]
            }
          ]
        }
      ]
    }
]
```

其中包含 3 个部分：

- `char` 表示当前汉字
- `details` 表示汉字的一般含义
- `pronunciations` 表示汉字在各个读音下的不同含义
- 如果是普通的描述用 ul 表示，如果是 1、2、3这种开头的表示一组描述，用 ol 表示

#### polyphone.json 多音字

polyphone.json 文件中的多音字包含常用字里多音字的 600 余个和其它非常用字的 1000 余个，共 1756 条数据。

```json
[
  {"index": 1, "char": "了", "pinyin": ["liǎo", "le"], "frequency": 0, "strokes": 2},
  {"index": 506, "char": "咖", "pinyin": ["kā", "gā"], "frequency": 2, "strokes": 8}
]
```

其中：

- `index` 表示数据索引值，从 1 开始
- `char` 表示该汉字
- `pinyin` 为汉字读音的数组
- `frequency` 表示使用频率，0 为最常用，1 为较常用，2 为次常用，3 为不常用
- `strokes` 表示汉字笔画数

## 线上应用

目前 **汉语拼音辞典** 已经在多端上线小程序。

微信小程序：汉语拼音辞典

<img alt="微信小程序" src="https://cdn.mapull.com/char/qrcode/wechat_character.jpg"></img>

百度小程序：码谱文字转拼音

<img alt="百度小程序" src="https://cdn.mapull.com/char/qrcode/baidu_character.png"></img>

抖音、字节跳动小程序：汉语拼音辞典

<img alt="字节跳动小程序" src="https://cdn.mapull.com/char/qrcode/toutiao_character.png"></img>

## 参考资料

字库的基础数据大都来自 Github 及其他开源组织，本项目字库参考但不限于如下资源：

- [Github] [funNLP](https://github.com/fighting41love/funNLP)
- [Github] [pinyin-data](https://github.com/mozillazg/pinyin-data)
- [Github] [chinese-xinhua](https://github.com/pwxcoo/chinese-xinhua)
- [Github] [phrase-pinyin-data](https://github.com/mozillazg/phrase-pinyin-data)
- [开源] [CC-CEDICT](https://www.mdbg.net/chinese/dictionary?page=cc-cedict)
- [官方] [中国语言文字网](http://www.china-language.edu.cn/)
- [商用] [汉典](https://www.zdic.net/)
- [商用] [字海，叶典网](http://zisea.com/)

> 参考商用数据是为了人工校对数据的准确性，并没有对其数据进行爬取。

## 版权

该项目是为了支持 **汉语拼音辞典** 的线上数据。在使用小程序的过程中，发现有些汉字读音有误，如果人工校对将是一个庞大的工程，于是对现有的开源语料库进行了多维分析。如果不确定的读音，还参考了部分商业应用如汉典网的数据进行人工比对。

本项目汇总得到的数据结果采用 MIT License 开源。

因为某些收集来的数据，无法确认数据的最初来源，使用它们可能存在风险。