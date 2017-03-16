import json
from numpy import genfromtxt, savetxt
import pandas as pd
import re

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        r"\<https.+?\>"                           
                           "]+", flags=re.UNICODE)



tweets_data = []
text_data=[]
text_wo_emoji=[]
coord=[]
geo=[]
language=[]
location=[]
time_zone=[]
geo_enabled=[]
place=[]
data=[]
data1=" "
with open('./output_1.txt','r') as f:
    for line in f:
        tweet = json.loads(line)
        tweets_data.append(tweet)
        
text_count=0
lang=''
for i in tweets_data:
    if 'created_at' in i.keys():
        if 'text' in i.keys():
            lang=i.get('lang')
            language.append(i.get('lang'))
            if lang=='en' and i.get('coordinates') is not None and i.get('place') is not None: 
                #print("english")
                text_data.append(i.get('text'))
#                c=i.get('coordinates')
#                if c is not None:
                coord.append(i.get('coordinates')['coordinates'])
                geo.append(i.get('geo')['coordinates'])
                location.append(i.get('user')['location'])
                time_zone.append(i.get('user')['time_zone'])
                geo_enabled.append(i.get('user')['geo_enabled'])
                place.append(i.get('place')['country'])

tweet_clean=[]
for i in range(len(text_data)):
    tweet_clean.append(re.sub('https?:\/\/(?:www\.|(?!www))[^\s\.]+\.[^\s]{2,}|www\.[^\s]+\.[^\s]{2,}','', text_data[i]))


for i in range(len(tweet_clean)):
    text_wo_emoji.append(emoji_pattern.sub(r'',tweet_clean[i]))

text_wo_hash=[]
for i in range(len(text_wo_emoji)):
    text_wo_hash.append(re.sub('?<=\s|^(#)\w*[A-Za-z_]+\w*','',text_wo_emoji[i]))

print(text_wo_hash)

data=[]
for i in range(len(text_data)):
#    print(i)
    row=[]
    row.append(text_data[i])
    row.append(coord[i])
    row.append(geo[i])
    row.append(location[i])
    row.append(time_zone[i])
    row.append(geo_enabled[i])
    row.append(place[i])
    data.append(str(row)[1:len(str(row))-1])


#data.append(text_data)
#data.append(coord)
#data.append(geo)
#data.append(location)
#data.append(time_zone)
#data.append(geo_enabled)
#data.append(place)
data1=''.join(str(e) for e in data)
with open('./data2.txt','w', encoding='utf-8') as f:
    f.write(data1+"\r\n")
    
