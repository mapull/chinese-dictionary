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
|----|----|----|---- char_base.json             总收录汉字 16146
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
		"char": "杈",
		"details": [
			{
				"ul": "(形声。从木，叉声。本义树干的分枝或树枝的分岔)"
			},
			{
				"ul": "同本义"
			},
			{
				"ul": "杈，杈枝也。--《说文》"
			},
			{
				"ul": "江东谓树枝为桠杈。--《方言》"
			},
			{
				"ul": "突杈枒而皆折，又有触邪之气也。--杜甫《雕赋》"
			},
			{
				"ul": "又如杈桠(杈丫；杈儿。树的分枝)"
			},
			{
				"ul": "叉状用具"
			}
		],
		"pronunciations": [
			{
				"pinyin": "chà",
				"texts": [
					{
						"ul": "植物干茎分枝或枝的再分树～。棉花～子。枝～儿。"
					}
				]
			},
			{
				"pinyin": "chā",
				"texts": [
					{
						"ul": "一种叉着稻草、麦秆或柴草等挑运的用具木～。"
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