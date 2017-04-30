# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 13:03:18 2017

@author: shant
"""

import csv
import re
#from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords #stopwords
from nltk.corpus import words # english vocabulary

special_char = ["!","$","%","^","&","*","(",")","[","]","{","}","|","\",""","\\",":",";","?","/",".",">",",","<","+","-","=","_"]
    
def preprocess(text):
#    text = [char for char in text if char not in special_char]
    text = re.sub(r'RT ','',text) #remove 'RT '
    text = re.sub(r"(@\S+)", "", text) #remove '@username: '
    text = re.sub(r"#\S+", "", text) # remove '#hashtag'
    text = re.sub(r'(&gt;|&lt;)',' ',text)
    text = re.sub(r'\.{2,}',' ',text)
    text = re.sub(r'\W+',' ', text) #remove special characters
    text = re.sub(r'[^\x00-\x7F]',' ',text) #remove extended ascii
    text = text.lower() #convert to lower
    text = text.split(' ') #split text
    text = [word for word in text if word not in stopwords.words('english')] #remove stopwords
    text = list(filter(lambda a: a != '', text)) #remove all ''
    #remove basic engliswords, len 850 vs 235886
    text = [word for word in text if word not in words.words('en-basic')]
    return text
    
    
all_text=[]
i=0
with open("je_2010.txt",encoding = "ISO-8859-1") as tsv:
    tsv = (x.replace('\0', '') for x in tsv)
    for test in csv.reader(tsv, delimiter="\t"): #You can also use delimiter="\t" rather than giving a dialect.
#        print('----------------------------------')
#        print(test[5])
        text = preprocess(test[5]) 
        print(text)
        i=i+1
        if i==1000:
#        all_text.append(test[5])
            break;

