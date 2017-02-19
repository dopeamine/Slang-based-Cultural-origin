import twitter
api = twitter.Api(consumer_key='cTmRksMMFZQq5QblvTGlpCNoD', consumer_secret='Q3HG3yUThn7pX6sa0x96dMfrm783d51s7Z3Ht8ifso2ql8GRiG', 
                  access_token_key='382748132-yn4EyksHJwAZ7pUkqnULZwLujWGzWgy48DRsq8oe', access_token_secret='wNMgaIO6WgQq0JOKbPIUBFMEzarREI9SsI09YvfxvApy4')

with open('output.txt', 'a') as f:
    # api.GetStreamFilter will return a generator that yields one status
    # message (i.e., Tweet) at a time as a JSON dictionary.
    
    #streaming api - gets a subset 
    for line in api.GetStreamSample(delimited=False, stall_warnings=True):
        f.write(json.dumps(line))
        f.write('\n')
        
def jlkjad():
    