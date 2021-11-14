# character

此文件夹中内容为单个汉字。

所有文件均为 JSON 格式。

### 目录结构

```text
|---- dbjson
|----|---- char_common.json      常用字 3500
|----|---- char_most.json        最常用字 500
|----|---- char_first.json       常用字 2000
|----|---- char_secondary.json   次常用字 1000
|----|---- polyphone.json        多音字 1756
```

常用字（3500） = 最常用字（500）+ 较常用字（2000）+ 次常用字（1500） 

### 数据格式

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

不是所有文件中含有 frequency 字段。

- char_most.json 中 frequency 字段为固定值 0
- char_first.json 中 frequency 字段为固定值 1
- char_secondary.json 中 frequency 字段为固定值 2

#### 多音字

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