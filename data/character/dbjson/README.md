# dbjson

此文件夹中内容是为特定数据库准备的 json 脚本。

某些数据库需要的 json 文件并非标准的 JSON 格式，而是每行一条数据，每行数据是一个标准的 JSONOBJECT，行末尾没有逗号。

### 目录结构

```text
|---- dbjson
|----|---- char_common.json      常用字 3500
|----|---- char_most_common.json 最常用字 2500
|----|---- char_secondary.json   次常用字 1000
```

### 数据格式

```json
{"index": "1010", "char": "Tom"}
{"index": "1011", "char": "Jack"}
{"index": "1012", "char": "Alex"}
```

- `index` 表示从 1 开始的自然增长序列，默认按照汉字笔画数排序。
- `char` 表示一个汉字。
- `frequency` 表示使用频率，1 为最常用，2 为次常用。