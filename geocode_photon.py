from geopy.geocoders import Photon
from geopy.point import Point
import csv

coords_by_state = {'ME': [],'VT': [],'NH': [],'NY': [],'MA': [],'CT': [],'RI': [],'PA': [],'NJ': [],'ND':[],'MN': [],'SD': [],'NE': [],'IA': [],'KS': [],'MO': [],'IL': [],'WI': [],'MI': [],'OH': [],'IN': [],'WA': [],'MT': [],'OR': [],'ID': [],'WY': [],'CA': [],'NV': [],'UT': [],'CO': [],'AZ': [],'NM': [],'OK': [],'TX': [],'AR': [],'LA': [],'KY': [],'TN': [],'MS': [],'AL': [],'WV': [],'VA': [],'MD': [],'DE': [],'NC': [],'SC': [],'GA': [],'FL': [],'AK': [],'HI':[] }


        geolocator = Photon()with open('latlong.csv') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    for row in reader:
        print(row)

        print(geolocator)
#        p = 
        result = geolocator.reverse(', '.join(row))
        print(result)
        break;
        
#photon.komoot.de/reverse?lon=47.5279679v&lat=-122.1976519