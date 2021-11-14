# 2021/11/07 - 13:53
import xlrd
import json


def parse_3500():
    """
    解析 3500 常用字
    """
    chars = []
    for content in open('tmp.txt', "r", encoding="utf-8"):
        splits = str.split(content, ' ')
        chars = splits
    print(len(chars))

    workbook = xlrd.open_workbook("hanzi.xls")
    sheet = workbook.sheets()[0]
    contents = []
    for i in range(5, sheet.nrows):
        row = sheet.row_values(i)
        char = row[1]
        dic = {"id": int(row[0]), "char": char, "frequency": int(row[2])}
        if char in chars:
            dic['frequency'] = 0
        contents.append(dic)
    print(len(contents))
    with open('char_common.json', "w", encoding="utf-8") as file:
        file.write(json.dumps(contents, ensure_ascii=False))


# def parse_2500():
#     """
#     解析 2500 最常用字
#     """
#     workbook = xlrd.open_workbook("hanzi.xls")
#     sheet = workbook.sheets()[0]
#     contents = []
#     idx = 0
#     for i in range(5, sheet.nrows):
#         row = sheet.row_values(i)
#         if row[2] == '1':
#             idx = idx + 1
#             dic = {"id": idx, "char": row[1]}
#             contents.append(dic)
#     with open('char_most_common.json', "w", encoding="utf-8") as file:
#         file.write(json.dumps(contents, ensure_ascii=False))
#
#
# def parse_1000():
#     """
#     解析 1000 次常用字
#     """
#     workbook = xlrd.open_workbook("hanzi.xls")
#     sheet = workbook.sheets()[0]
#     contents = []
#     idx = 0
#     for i in range(5, sheet.nrows):
#         row = sheet.row_values(i)
#         if row[2] == '2':
#             idx = idx + 1
#             dic = {"id": idx, "char": row[1]}
#             contents.append(dic)
#     with open('char_secondary.json', "w", encoding="utf-8") as file:
#         file.write(json.dumps(contents, ensure_ascii=False))


if __name__ == "__main__":
    # parse_1000()
    # parse_2500()
    parse_3500()
