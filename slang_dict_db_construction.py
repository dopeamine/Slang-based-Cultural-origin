# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 14:10:12 2017

@author: shant
"""

import csv
import sqlite3

#for i in range(1,5):
#    print(i)
#    with open('slang_dictionary/urban_dictionary_.csv') as csvfile:

connection = sqlite3.connect('slangdictionary.db')
c = connection.cursor()

c.execute('''CREATE TABLE slangdict (word text, meaning text, example text)''')


for i in range(1,5):    
    with open('slang_dictionary/urban_dictionary_'+str(i)+'.csv', encoding='utf-8') as csvfile:
        dictionary = csv.reader(csvfile)
    #    print(dictionary)
        for row in dictionary:
    #        c.execute("INSERT INTO slangdict VALUES ("+row[0]+","+row[4]+","+row[5]+")")
            data = [row[0],row[4],row[5]]
            c.execute("INSERT INTO slangdict VALUES (?,?,?)", data)

connection.commit()
c.close()
connection.close()
#for row in c.execute('SELECT * FROM slangdict'):
#        print(row)