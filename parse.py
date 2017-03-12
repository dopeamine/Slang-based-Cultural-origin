import json

tweets_data = []
text_data=[]
with open('./output.txt','r') as f:
    for line in f:
        tweet = json.loads(line)
        tweets_data.append(tweet)
        
text_count=0
lang=''
for i in tweets_data:
    if 'created_at' in i.keys():
        if 'text' in i.keys():
            lang=i.get('lang')
            if lang=='en':
                #print("english")
                text_data.append(i.get('text','geo.coordinates'))
#    if 'user' in i.keys():
#        total_tweets+=1
#        if i['place'] != None:
#            #count_country_mentioned+=1
#print(count_country_mentioned,total_tweets)

data=''.join(text_data)
with open('./data.txt','w') as f:
    f.write(data)

#print(text_count)

#res =[]
#for i in tweets_data:
#    if 'created_at' in i.keys():
#       print(list(i.keys()).count('text'))