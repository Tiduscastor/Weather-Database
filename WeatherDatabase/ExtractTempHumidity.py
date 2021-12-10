# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 23:07:24 2021

@author: Patrick Wesley
"""

#Purpose: Extract temperature, humidity data from weather database into CSV file
# Run BuildWeatherDB.py to build weather database before running this program

import sqlite3

def convertCtoF(tempC):#convert Celsius temperature to Fahrenheit
    return (tempC*9.0/5.0) + 32.0

dbFile = "weather_B.db" #file names for database and output file
output_file_name ='formatdata_B.csv'#connect to and query weather database
#added a 2 for list distinction

dbFile = "weather_B.db"
conn = sqlite3.connect(dbFile)
cur = conn.cursor()#create cursor to execute SQL commands
selectCmd = """ SELECT temperature, relativeHumidity FROM observations
            ORDER BY timestamp; """

cur.execute(selectCmd)
allRows = cur.fetchall()
#limit the number of rows output to half
rowCount = len(allRows)//2 # double slash does integer division
rows = allRows[rowCount:] #changed the : from before to after rowCount for second list

#write data to output file
with open(output_file_name,"w+") as outf:
    outf.write('Celsius,Fahrenheit,Humidity')
    outf.write('\n')
    for row in rows:
        tempC = row[0]
        if tempC is None: #handle missing temperature value
           outf.write(',,')
        else:
            tempF = convertCtoF(tempC)
            outf.write(str(tempC)+',')
            outf.write(str(tempF)+',')

        humidity = row[1]
        if humidity is None: #handle missing humidity value
           outf.write('\n')
        else:
           outf.write(str(humidity)+'\n') #print data to file separated by commas