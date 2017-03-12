import json

tweets_data = []
with open('./output.txt','r') as f:
    for line in f:
        print(line)
        tweet = json.loads(line)
        tweets_data.append(tweet)
        
count_country_mentioned=0
total_tweets=0
for i in tweets_data:
    if 'user' in i.keys():
        total_tweets+=1
        if i['place'] != None:
            count_country_mentioned+=1
print(count_country_mentioned,total_tweets)

res =[]
for i in tweets_data:
    if 'created_at' in i.keys():
       print(list(i.keys()).count('text'))
       
#def easy(root):
#    
#    if type(root)==dict:
#        for i in root.keys():
#            print("sad",i)
#            easy(i)
#    else:
#        print("dfa",root)
#easy(tweets_data[0])