# dbjson

此文件夹中内容是为特定数据库准备的 json 脚本。

某些数据库需要的 json 文件并非标准的 JSON 格式，而是每行一条数据，每行数据是一个标准的 JSONOBJECT，行末尾没有逗号。

### 目录结构

```text
|---- dbjson
|----|---- char_common.json      常用字 3500
|----|---- polyphone.json        多音字 1756
```

### 数据格式

#### char_common.json 常用字

```json
{"index": 1, "char": "一", "frequency": 1}
{"index": 2, "char": "乙", "frequency": 1}
```

- `index` 表示从 1 开始的自然增长序列，默认按照汉字笔画数排序。
- `char` 表示一个汉字。
- `frequency` 表示使用频率，0 为最常用，1 为常用，2为次常用。

#### polyphone.json 多音字

```json
{"index": 1, "char": "了", "pinyin": ["liǎo", "le"], "frequency": 0, "strokes": 2}
{"index": 4, "char": "厂", "pinyin": ["chǎng", "ān", "hàn"], "frequency": 0, "strokes": 2}
```