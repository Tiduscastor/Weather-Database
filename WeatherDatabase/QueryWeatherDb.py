# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 22:10:14 2021
@author: patri
"""

# Purpose: Query database using SQL
# Name: Patrick Wesley
# Edited Date: 01/04/2024
# Run BuildWeatherDB.py to build the weather database before running this program

import sqlite3
import pandas as pd

# File names for the database and output file

db_file = "weather_B.db"

# Format output

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)

# Connect to and query the weather database

conn = sqlite3.connect(db_file)

# Create SQL command

select_cmd = " SELECT * FROM observations ORDER BY timestamp; "
# "SELECT temperature, windspeed, textDescription FROM observations where textDescription = 'Clear'; "
# " SELECT MIN(temperature), MAX(temperature) FROM observations; "

# Print out the query

result = pd.read_sql_query(select_cmd, conn)
print(result)
