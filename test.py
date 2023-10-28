import pandas as pd
import sqlite3

# Connect to a SQLite database (creates a new one if it doesn't exist)
connection = sqlite3.connect("test.db")
cursor = connection.cursor()

df = pd.read_csv('trips.csv')

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS trips (
                    id INTEGER PRIMARY KEY,
                    region TEXT,
                    origin_lat REAL,
                    origin_lon REAL,
                    destination_lat REAL,
                    destination_lon REAL,
                    datetime DATETIME,
                    datasource TEXT
                 )''')

# Iterate over the DataFrame and insert each row into the database
for index, row in df.iterrows():
    region = row['region']
    origin_coord = row['origin_coord']
    destination_coord = row['destination_coord']
    datetime = row['datetime']
    datasource = row['datasource']

    # Extract latitude and longitude from origin and destination coordinates
    origin_lat, origin_lon = map(float, origin_coord.strip('POINT ()').split())
    destination_lat, destination_lon = map(float, destination_coord.strip('POINT ()').split())

    # Define the SQL INSERT statement
    insert_statement = """
    INSERT INTO trips (region, origin_lat, origin_lon, destination_lat, destination_lon, datetime, datasource)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """

    # Execute the INSERT statement for the current row
    cursor.execute(insert_statement,
                   (region, origin_lat, origin_lon, destination_lat, destination_lon, datetime, datasource))

# Define the region of interest
region_name = 'Turin'

# Write the SQL query to calculate the weekly average by region
query = f"""
    SELECT strftime('%Y-%W', datetime) AS week, COUNT(*) AS trip_count
    FROM trips
    WHERE region = ?
    GROUP BY week
    """

# Execute the query
cursor.execute(query, (region_name,))

# Fetch the results
weekly_data = cursor.fetchall()

# Calculate the weekly average
total_trips = sum(trip_count for week, trip_count in weekly_data)
weeks = [w for w, v in weekly_data]
average_trips = total_trips / len(weekly_data) if weekly_data else 0

# Print the weekly average
print(f"Total trips: {total_trips} ")
print(f"Weeks: {weeks} ")
print(f"Weekly Average Number of Trips for {region_name} : {average_trips:.2f}")

# Commit and close the connection
connection.commit()
connection.close()
