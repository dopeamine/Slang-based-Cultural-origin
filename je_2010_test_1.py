import pandas as pd
import numpy as np
import geocoder as gd
import requests
import time 
import csv
import reverse_geocoder as rg
from geopy.geocoders import Nominatim

divisions = {'northeast' : ['ME','VT','NH','NY','MA','CT','RI','PA','NJ'],
             'midwest': ['ND','MN','SD','NE','IA','KS','MO','IL','WI','MI','OH','IN'],
             'west': ['WA','MT','OR','ID','WY','CA','NV','UT','CO','AZ','NM'],
             'south': ['OK','TX','AR','LA','KY','TN','MS','AL','WV','VA','MD','DE','NC','SC','GA','FL'],
             'pacific': ['AK','HI']
             }

#assert no of states
#len(divisions['northeast'])+len(divisions['midwest'])+len(divisions['west'])+len(divisions['south'])+len(divisions['pacific'])

#data = open('je_2010.txt',encoding = "ISO-8859-1", delimiter='\t')
main = {'user':[], 'timestamp':[],'location':[],'tweet':[],'state':[]}
coords_by_state = {'ME': [],'VT': [],'NH': [],'NY': [],'MA': [],'CT': [],'RI': [],'PA': [],'NJ': [],'ND':[],'MN': [],'SD': [],'NE': [],'IA': [],'KS': [],'MO': [],'IL': [],'WI': [],'MI': [],'OH': [],'IN': [],'WA': [],'MT': [],'OR': [],'ID': [],'WY': [],'CA': [],'NV': [],'UT': [],'CO': [],'AZ': [],'NM': [],'OK': [],'TX': [],'AR': [],'LA': [],'KY': [],'TN': [],'MS': [],'AL': [],'WV': [],'VA': [],'MD': [],'DE': [],'NC': [],'SC': [],'GA': [],'FL': [],'AK': [],'HI':[] }

def check_coord_in_state(location):
    for state in coords_by_state:
        if location in coords_by_state[state]:
            return state
    return False

i=0
j=0
coord = []
corrupted=[]

#check for null bytes
#with open("je_2010.txt",encoding = "ISO-8859-1") as tsv:
#    if '\0' in tsv.read():
#        print ("you have null bytes in your input file")
#    else:
#        print ("you don't")
i=0
geolocator = Nominatim()
with requests.Session() as session:
    with open("je_2010.txt",encoding = "ISO-8859-1") as tsv:
        tsv = (x.replace('\0', '') for x in tsv)
        with open('latlong.csv','w',newline='') as csvfile:
            latlong_writer = csv.writer(csvfile,delimiter=',')
            for test in csv.reader(tsv, delimiter="\t"): #You can also use delimiter="\t" rather than giving a dialect.
    #            print(test)
    #            test = line.split()
                location = [test[3],test[4]]
                
#            location = geolocator.reverse(test[3]+","+test[4])
#            state=location
#            test = location.address.replace(', ',',').split(',')
#            state=test[-3]
#            time.sleep(1)
#            print(state)
#            break;
#            print(location)
#            test = [test[0],test[1],test[3]," ".join(test[6:])]
        #    print(test)
#            main['user'].append(test[0])
#            main['timestamp'].append(test[1])
#            main['location'].append(location)
#            main['tweet'].append(test[5])
#            location = test[2].split(',')
#            print(location)
#            if len(location)==2 and location[1]!='':
#                location = list(map(float, location))
                if location not in coord:
                    coord.append(location)
                    latlong_writer.writerow(location)
                    i+=1
                    print(i,location)
#                    if i==100:
#                        break;
                
#            else:
#                if location not in corrupted:
#                    corrupted.append(location)
#                print(location)
#            coord_in_state = check_coord_in_state(location)
#            print(coord_in_state)
#            if not coord_in_state:
#                print(True)
#                g = gd.google(location,method='reverse',session=session)
#                time.sleep(2)
#                if g.state in coords_by_state:
##            print(g.state,location)
#                    coords_by_state[g.state].append(location)
#                    main['state'].append(g.state)
#                    print("A: ",i,g.state,g.ok)
#                    
#                    i=i+1
#                else:
#                    j+=1
#                    print("B: ",j,g.state,g.ok)
#                    print(g.json)
##                    print("-------------------------------------------------------------------J=",j,g.state)
#            else:
##                print(False)
#                main['state'].append(coord_in_state)
#            if g.state not in coords_by_state:
#                coo
#            print(check_coord_in_state(location))

        #        
        #    print(location[0],test[4],location[0]==test[4],location[1],test[5],location[1]==test[5])
        #    if location[0]!=test[4] or location[1]!=test[5]:
        #        print("False")

#testframe = pd.DataFrame(main)
#testframe.to_excel('state_labels.xlsx', sheet_name='Sheet1')
#(divisions['northeast'])+(divisions['midwest'])+(divisions['west'])+(divisions['south'])+(divisions['pacific'])