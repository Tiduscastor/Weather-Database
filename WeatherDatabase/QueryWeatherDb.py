# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 22:10:14 2021

@author: patri
"""

#Purpose: Query database using SQL
#Name: Your name
#Date: Your date
# Run BuildWeatherDB.py to build weather database before running this program

import sqlite3
import pandas as pd

#file names for database and output file

dbFile = "weather_B.db"

#format output

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)

#connect to and query weather database

conn = sqlite3.connect(dbFile)

#Create SQL command

selectCmd = " SELECT * FROM observations ORDER BY timestamp; "
#"SELECT temperature, windspeed, textDescription FROM observations where textDescription = 'Clear'; "
#" SELECT MIN(temperature), MAX(temperature) FROM observations; " 

#print out the query

result = pd.read_sql_query(selectCmd, conn)
print(result)