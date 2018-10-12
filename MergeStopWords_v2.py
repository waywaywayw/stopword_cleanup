# -*- coding: utf-8 -*-
"""
@author: weijiawei
@date: 2018-10-11
"""
import os
import re
from collections import Counter
from atools_python.files import MyFiles

# 获取停用词的List
def GetListOfStopWords(filepath):
    f_stop = open(filepath, 'r', encoding='utf8')
    try:
        f_stop_text = f_stop.read()
    finally:
        f_stop.close()
    f_stop_seg_list = f_stop_text.split('\n')

    f_stop_seg_list = [x.strip() for x in f_stop_seg_list if len(x.strip())>0]
    return f_stop_seg_list


# 保存List
def SaveFile(list, filename):
    f_stop = open(filename, 'w', encoding='utf8')
    for item in list:
        f_stop.write(item+'\n')
    f_stop.close()


# 求List并集
def GetListUnion(word_list, word_cnt):
    for word in word_list:
        word_cnt[word] += 1
    return word_cnt


if __name__ == "__main__":
    # 需要遍历的文件夹
    need_folders = ['stopwords', 'stopwords-list', '停用词整理']
    # need_folders = ['test']

    # 统计停用词
    word_cnt = Counter()
    for folder in need_folders:
        for file in MyFiles(os.path.join('stopword', folder)):
            # 获取单个文件中的停用词
            word_list = GetListOfStopWords(file)
            # 合并停用词列表（保留 单词、频率）
            word_cnt = GetListUnion(word_list, word_cnt)
            # debug
            # break
        # break

    # 去掉频率较低的停用词（可选）
    threshold = 0   # 小于阈值的词去掉
    word_cnt = [x for x,p in word_cnt.items() if p>threshold]

    # 只保留中文词（可选）
    word_cnt = list(filter(lambda x: re.match(r'[\u4E00-\u9FD5]+$', x), word_cnt))
    # word_cnt = list(word_cnt)

    # 排序并保存
    word_cnt.sort()
    SaveFile(word_cnt, os.path.join('output',"stopwords_CN.txt"))
