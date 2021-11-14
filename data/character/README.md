# character

此文件夹中内容为单个汉字。

所有文件均为 JSON 格式。

### 目录结构

```text
|---- dbjson
|----|---- char_base.json        汉字 16146
|----|---- char_common.json      常用字 3500
|----|---- polyphone.json        多音字 1756
```

常用字（3500） = 最常用字（500）+ 较常用字（2000）+ 次常用字（1500） 

### 数据格式

#### char_base.json 基础汉字

```json
[
  {"index": 1, "char": "一", "strokes": 1, "pinyin": ["yī"], "radicals": "一", "frequency": 0}, 
  {"index": 2770, "char": "咧", "strokes": 9, "pinyin": ["liě", "liē", "lié", "lie"], "radicals": "口", "frequency": 2}
  {"index": 7467, "char": "砭", "strokes": 9, "pinyin": ["biān"], "radicals": "石", "frequency": 3}
]
```


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

#### polyphone.json 多音字

polyphone.json 文件中的多音字包含常用字里多音字的 600 余个和其它非常用字的 1000 余个，共 1756 条数据。

```json
[
  {"index": 1, "char": "了", "pinyin": ["liǎo", "le"], "frequency": 0, "strokes": 2},
  {"index": 506, "char": "咖", "pinyin": ["kā", "gā"], "frequency": 2, "strokes": 8}
]
```

其中：

- index 表示数据索引值，从 1 开始
- char 表示该汉字
- pinyin 为汉字读音的数组
- frequency 表示使用频率，0 为最常用，1 为较常用，2 为次常用
- strokes 表示汉字笔画数