from geopy.geocoders import Photon
from geopy.point import Point
import csv

states = {"AK": "ALASKA",
"AL": "ALABAMA",
"AR": "ARKANSAS",
"AS": "AMERICAN SAMOA",
"AZ": "ARIZONA",
"CA": "CALIFORNIA",
"CO": "COLORADO",
"CT": "CONNECTICUT",
"DC": "DISTRICT OF COLUMBIA",
"DE": "DELAWARE",
"FL": "FLORIDA",
"GA": "GEORGIA",
"GU": "GUAM",
"HI": "HAWAII",
"IA": "IOWA",
"ID": "IDAHO",
"IL": "ILLINOIS",
"IN": "INDIANA",
"KS": "KANSAS",
"KY": "KENTUCKY",
"LA": "LOUISIANA",
"MA": "MASSACHUSETTS",
"MD": "MARYLAND",
"ME": "MAINE",
"MI": "MICHIGAN",
"MN": "MINNESOTA",
"MO": "MISSOURI",
"MS": "MISSISSIPPI",
"MT": "MONTANA",
"NC": "NORTH CAROLINA",
"ND": "NORTH DAKOTA",
"NE": "NEBRASKA",
"NH": "NEW HAMPSHIRE",
"NJ": "NEW JERSEY",
"NM": "NEW MEXICO",
"NV": "NEVADA",
"NY": "NEW YORK",
"OH": "OHIO",
"OK": "OKLAHOMA",
"OR": "OREGON",
"PA": "PENNSYLVANIA",
"PR": "PUERTO RICO",
"RI": "RHODE ISLAND",
"SC": "SOUTH CAROLINA",
"SD": "SOUTH DAKOTA",
"TN": "TENNESSEE",
"TX": "TEXAS",
"UT": "UTAH",
"VA": "VIRGINIA",
"VI": "VIRGIN ISLANDS",
"VT": "VERMONT",
"WA": "WASHINGTON",
"WI": "WISCONSIN",
"WV": "WEST VIRGINIA",
"WY": "WYOMING"}
coords = {}
unique_countries ={}
with open('latlong_labeled.csv') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    i=0
    for row in reader:
        if i>0:
            key = row[0]+","+row[1]
            print(key)
#            if row[2]=='United States':
            if key not in coords:
                coords[key]=[]
                coords[key].append(row[2])
            else:
                coords[key].append(row[2])
        i=i+1
#        break;
            
        
countries = [coords[key][0] for key in coords]
unique_countries = {country: countries.count(country) for country in countries if country not in unique_countries}

us_coords = {location: coords[location] for location in coords if coords[location][0]=="United States"}

def retrieveStateAbrv(state):
    for key in states:
        if states[key]==state:
            return key
    
def findState(text):
    text = " ".join(text)
    text = text.upper()
    for value in states.values():
        result = text.find(value)
        if result == -1:
            continue;
        else:
            print(value,result)
            return retrieveStateAbrv(value)
    
    for key in states.keys():
        result = text.find(key)
        if result == -1:
            continue;
        else:
            print(key,result)
            return key
        
#[1 for location in us_coords_only_state if us_coords_only_state[location]==None]    #check no of Nones due to only us in array
#[1 for location in us_coords_only_state if us_coords_only_state[location] != None and len(us_coords_only_state[location])==2]        #any abbreviated labels?
        
us_coords_only_state = {location: findState(us_coords[location][1:]) for location in us_coords if len(us_coords[location])>4}
        
with open('latlong_us_only_state_abrv.csv','w',newline='') as csvfile:
    latlong_writer = csv.writer(csvfile,delimiter=',')
    for location in us_coords_only_state:
        temp = location.split(',')
        temp = [temp[0],temp[1],us_coords_only_state[location]]
        latlong_writer.writerow(temp)
        
        
#with open('latlong_labeled.csv') as csvfile:
#    reader = csv.reader(csvfile,delimiter=',')
#    for row in reader:
#        key = row[0]+","+row[1]
#        if coords[key][0] == 'United States':
#            test_row = [row[0]]+[row[1]]+[coords[key][0]]
#            temp = ' '.join(coords[key][1:])
#            if temp.find()
#{'Bahamas': 1,
# 'Bermuda': 10,
# 'Brazil': 1,
# 'Canada': 1180,
# 'China': 1,
# 'Colombia': 5,
# 'Dominican Republic': 15,
# 'France': 1,
# 'Germany': 1,
# 'India': 5,
# 'Indonesia': 23,
# 'Mexico': 126,
# 'Puerto Rico': 1,
# 'Russia': 2,
# 'Saudi Arabia': 6,
# 'Scotland': 4,
# 'South Africa': 8,
# 'Taiwan': 1,
# 'Thailand': 6,
# 'United States': 44829,
# 'name': 1}