from config import Config


class Analytics(Config):
    """
    Class to call the class Etl Process
    """

    def __init__(self):
        """
        Constructor
        """
        self.config()

    def group_data(self):

        region_name = 'Turin'

        # Write the SQL query to calculate the weekly average by region
        query = f"""
            SELECT strftime('%Y-%W', datetime) AS week, COUNT(*) AS trip_count
            FROM trips
            WHERE region = 'Turin'
            GROUP BY week
            """
        # Execute the query
        self._execute_query(query)

"""
        # Calculate the weekly average
        total_trips = sum(trip_count for week, trip_count in weekly_data)
        weeks = [w for w, v in weekly_data]
        average_trips = total_trips / len(weekly_data) if weekly_data else 0

        # Print the weekly average
        print(f"Total trips: {total_trips} ")
        print(f"Weeks: {weeks} ")
        print(f"Weekly Average Number of Trips for {region_name} : {average_trips:.2f}")
"""