import twitter
import pandas as pd
import json

api = twitter.Api(consumer_key='cTmRksMMFZQq5QblvTGlpCNoD', consumer_secret='Q3HG3yUThn7pX6sa0x96dMfrm783d51s7Z3Ht8ifso2ql8GRiG',
                  access_token_key='382748132-yn4EyksHJwAZ7pUkqnULZwLujWGzWgy48DRsq8oe', access_token_secret='wNMgaIO6WgQq0JOKbPIUBFMEzarREI9SsI09YvfxvApy4')

with open('output_test_042717.txt', 'a') as f:
    # api.GetStreamFilter will return a generator that yields one status
    # message (i.e., Tweet) at a time as a JSON dictionary.

    #streaming api - gets a subset
    for line in api.GetStreamSample(delimited=False, stall_warnings=True):
        f.write(json.dumps(line))
        f.write('\n')

#    api.
#all_nc_users=[]
#all_cali_users=[]
#test_frame = pd.DataFrame(columns=['id','tweets','location'])
#
## search for users containing North Carolina
#for i in range(40):
#    nc_users = api.GetUsersSearch("north carolina",count=100,page=i)
#    cali_users = api.GetUsersSearch("california",count=100,page=i)
#    all_nc_users = all_nc_users+nc_users
#    all_cali_users = all_cali_users+cali_users
#
#
##get north carolina users
## for user in all_nc_users:
##     test_frame['id']=user.id
##     statuses = api.GetUserTimeline(user.id,count=200,include_rts=False)
##     print([s.text for s in stat uses])
##     test_frame['tweets']=[s.text for s in statuses]
##     test_frame['location']='NC'
##     print(len(statuses))
#
## #get california users
## for user in all_cali_users:
##     statuses = api.GetUserTimeline(user.id,count=200,include_rts=False)
##     print([s.text for s in statuses])
##     print(len(statuses))
