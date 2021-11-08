# dbjson

此文件夹中内容是为特定数据库准备的 json 脚本。

某些数据库需要的 json 文件并非标准的 JSON 格式，而是每行一条数据，每行数据是一个标准的 JSONOBJECT，行末尾没有逗号。

类似如下格式：

```json
{"id": "1010", "name": "Tom"}
{"id": "1011", "name": "Jack"}
{"id": "1012", "name": "Alex"}
```