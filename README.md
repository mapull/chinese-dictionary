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
|----|----|----|---- char_all.json       总收录汉字 16146
|----|----|----|---- char_common.json    常用字 3500
|----|----|----|---- char_most_common.json  最常用字 2500
|----|----|----|---- char_secondary.json    次常用字 1000
|----|---- scripts    脚本
```

### 为何数据是 JSON 格式

JSON 格式可以方便快捷地转为各种编程语言内部可使用的结构。

## 线上应用

目前 **汉语拼音辞典** 已经在多端上线小程序。

微信小程序：汉语拼音辞典

![微信小程序](https://cdn.mapull.com/char/qrcode/wechat_character.jpg)

百度小程序：码谱文字转拼音

![百度小程序](https://cdn.mapull.com/char/qrcode/baidu_character.png)

抖音、字节跳动小程序：汉语拼音辞典

![字节跳动小程序](https://cdn.mapull.com/char/qrcode/toutiao_character.png)


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

该项目是为了支持 **汉语拼音辞典** 的线上数据。在使用小程序的过程中，发现有些汉字读音有误，如果人工校队将是一个庞大的工程，于是对现有的开源语料库进行了多维分析。如果不确定的读音，还参考了部分商业应用如汉典网的数据进行人工比对。

本项目汇总得到的数据结果采用 MIT License 开源。

并不是说这些数据商业使用没有风险，因为某些收集来的数据，无法确认数据的最初来源，使用它们可能带来风险。