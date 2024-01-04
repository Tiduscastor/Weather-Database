# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 23:07:24 2021
@author: Patrick Wesley
"""
# Edited on 01/04/2024
# Purpose: Extract temperature, humidity data from weather database into CSV file
# Run BuildWeatherDB.py to build the weather database before running this program

import sqlite3

def convert_c_to_f(temp_c):  # Convert Celsius temperature to Fahrenheit
    return (temp_c * 9.0 / 5.0) + 32.0

db_file = "weather_B.db"  # File names for the database and output file
output_file_name = 'formatdata_B.csv'  # Connect to and query the weather database
# Added a 2 for list distinction

conn = sqlite3.connect(db_file)
cur = conn.cursor()  # Create a cursor to execute SQL commands
select_cmd = """ SELECT temperature, relativeHumidity FROM observations
            ORDER BY timestamp; """

cur.execute(select_cmd)
all_rows = cur.fetchall()
# Limit the number of rows output to half
row_count = len(all_rows) // 2  # Double slash does integer division
rows = all_rows[row_count:]  # Changed the : from before to after row_count for the second list

# Write data to the output file
with open(output_file_name, "w+") as outf:
    outf.write('Celsius,Fahrenheit,Humidity')
    outf.write('\n')
    for row in rows:
        temp_c = row[0]
        if temp_c is None:  # Handle missing temperature value
            outf.write(',,')
        else:
            temp_f = convert_c_to_f(temp_c)
            outf.write(f"{temp_c},{temp_f},")

        humidity = row[1]
        if humidity is None:  # Handle missing humidity value
            outf.write('\n')
        else:
            outf.write(f"{humidity}\n")  # Print data to file separated by commas
