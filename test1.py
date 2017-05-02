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
   
regions = {'northeast' : ['ME','VT','NH','NY','MA','CT','RI','PA','NJ'],
             'midwest': ['ND','MN','SD','NE','IA','KS','MO','IL','WI','MI','OH','IN'],
             'west': ['WA','MT','OR','ID','WY','CA','NV','UT','CO','AZ','NM'],
             'south': ['OK','TX','AR','LA','KY','TN','MS','AL','WV','VA','MD','DE','NC','SC','GA','FL'],
             'pacific': ['AK','HI']
             } 

def findRegion(state):
    for region in regions:
        if state in regions[region]:
            return region
    return False

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
us_coord_only = {}
with open('latlong_us_only_state_abrv.csv') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    for row in reader:
        location = row[0]+","+row[1]
        us_coord_only[location] = row[2]
        
i=0
with open("je_2010.txt",encoding = "ISO-8859-1") as tsv:
    tsv = (x.replace('\0', '') for x in tsv)
    with open('main_data.csv','w',newline='') as csvfile:
        main_data_writer = csv.writer(csvfile,delimiter=',')
        for test in csv.reader(tsv, delimiter="\t"): #You can also use delimiter="\t" rather than giving a dialect.
    #        print('----------------------------------')
#            print(test)
            user_id = test[0]
            tweet_text = preprocess(test[5])
            location = test[3]+","+test[4]
            if location in us_coord_only:
                state = us_coord_only[location]
                region = findRegion(state)
                main_data = [user_id, tweet_text, test[3],test[4],state, region]
#                print(tweet_text)
                main_data_writer.writerow(main_data)
#                i=i+1
#                if i==10:
    #        all_text.append(test[5])
#                    break;

