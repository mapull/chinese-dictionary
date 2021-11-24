# character

此文件夹中内容为单个汉字。

所有文件均为 JSON 格式。

### 目录结构

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

常用字（3500） = 最常用字（500）+ 较常用字（2000）+ 次常用字（1500） 

### 数据格式

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