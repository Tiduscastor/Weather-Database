# Purpose: Build weather database from NOAA data
# Name: Patrick Wesley
# Date: 11/11/2021
# Edited on: 01/04/2024
# See https://pypi.org/project/noaa-sdk/ for details on noaa_sdk package used

from noaa_sdk import noaa
import sqlite3
import datetime

# Parameters for retrieving NOAA weather data
zip_code = "37167"  # change to your postal code
country = "US"

# Date-time format is yyyy-mm-ddThh:mm:ssZ, times are Zulu time (GMT)
# Gets the most recent 14 days of data
today = datetime.datetime.now()
past = today - datetime.timedelta(days=14)
start_date = past.strftime("%Y-%m-%dT00:00:00Z")
end_date = today.strftime("%Y-%m-%dT23:59:59Z")

# Create connection - this creates a database if not exist
print("Preparing database...")
db_file = "weather_B.db"
conn = sqlite3.connect(db_file)

# Create cursor to execute SQL commands
cur = conn.cursor()

# Drop the previous version of the table if any, so we start fresh each time
drop_table_cmd = "DROP TABLE IF EXISTS observations;"
cur.execute(drop_table_cmd)

# Create a new table to store observations
create_table_cmd = """ CREATE TABLE IF NOT EXISTS observations (
timestamp TEXT NOT NULL PRIMARY KEY,
windSpeed REAL,
temperature REAL,
relativeHumidity REAL,
windDirection INTEGER,
barometricPressure INTEGER,
visibility INTEGER,
textDescription TEXT
) ; """
cur.execute(create_table_cmd)
print("Database prepared")

# Get hourly weather observations from NOAA Weather Service API
print("Getting weather data...")
n = noaa.NOAA()
observations = n.get_observations(zip_code, country, start_date, end_date)

# Populate the table with weather observations
print("Inserting rows...")

insert_cmd = """ INSERT INTO observations
(timestamp, windSpeed, temperature, relativeHumidity,
windDirection, barometricPressure, visibility, textDescription)
VALUES
(?, ?, ?, ?, ?, ?, ?, ?) """

count = 0
for obs in observations:
    insert_values = (
        obs["timestamp"],
        obs["windSpeed"]["value"],
        obs["temperature"]["value"],
        obs["relativeHumidity"]["value"],
        obs["windDirection"]["value"],
        obs["barometricPressure"]["value"],
        obs["visibility"]["value"],
        obs["textDescription"],
    )
    cur.execute(insert_cmd, insert_values)
    count += 1

if count > 0:
    cur.execute("COMMIT;")
    print(count, "rows inserted")
    print("Database load complete!")
