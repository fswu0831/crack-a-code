import json
import pandas as pd
import numpy as np
import mojimoji
import itertools
import re

class Encryption:
    def  __init__(self,doc):
        self.doc_list = []
        self.other_lang_count = 0
        self.create_doc_list(doc)
    
    def create_doc_list(self,doc):
        new_doc = mojimoji.zen_to_han(doc) # 全角を半角に変換
        Large_range = range(65,91)
        Small_range = range(97,123)
        Number_range = range(48,58)
        Signal_range = list(itertools.chain(range(33,48),range(58,65)))      
        
        
        for i in range(1,26):
            words = ''
            other_lang_count = 0
            for char in list(new_doc):
                ASCII = ord(char)
                temp = ''
                if ASCII in Signal_range:
                    # シグナルのときはshiftしない
                    temp = chr(ASCII)
                elif ASCII in Large_range:
                    temp = self.shift(ASCII,Large_range,i)
                elif ASCII in Small_range:
                    temp = self.shift(ASCII,Small_range,i)
                elif ASCII in Number_range:
                    temp = self.shift(ASCII,Number_range,i)
                elif ASCII == 32:
                    temp = chr(ASCII)
                else:
                    other_lang_count += 1
                    ASCII+=i
                    temp = chr(ASCII)
                    
                words += temp
            
            self.doc_list.append(words)
        self.other_lang_count = other_lang_count
        return
            
    def shift(self,ASCII,r_range,i):
        new_ASCII = ASCII + i
        while new_ASCII > r_range[-1]:
            new_ASCII = new_ASCII - r_range[-1] + r_range[0] -1
        return chr(new_ASCII)
    
    def get_docs(self):
        return self.doc_list
    
    def get_other_lang(self):
        return self.other_lang_count
    
    def get_other_lang_late(self):
        return self.other_lang_count / len(self.doc_list[0])

def calc_score(docs):
    words_list = [
        "I","my","me","this","that","these","those","all","each","some","any",
        "who","which","whose","who","a","one","an","you","your","he","his","him","the",
        "it","its","what","she","her","hers","are","is","will","were","am","be","was"
    ]
    score_list = []
    for doc in docs:
        score = 0
        words = re.split('[, !?/"/.]',doc) # , ? ! Space .で分割
        if len(words)>20:
            words = words[:20]
        for word in words:
            if word.lower() in words_list:
                score +=1
        score_list.append(score)
    return score_list