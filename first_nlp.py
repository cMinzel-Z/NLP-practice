# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:00:17 2020

@author: Minzel
"""
# Chinese NLP package
import jieba

str = '我在卡迪夫读书'

res = ' '.join(jieba.cut(str))

print(res)