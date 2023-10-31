from etl_process import EtlProcess


class WeekData(EtlProcess):
    """
    Class to call the class Etl Process
    """

    def __init__(self, result):
        """
        Constructor
        """
        self.result = result

    def _data_calculations(self):

        region_name = 'Turin'
        weekly_data = self.result

        # Calculate the weekly average
        total_trips = sum(trip_count for week, trip_count in weekly_data)
        weeks = [w for w, v in weekly_data]
        average_trips = total_trips / len(weekly_data) if weekly_data else 0

        # Print the weekly average
        self.logger.info(f"WEEKLY AVERAGE NUMBER OF TRIPS ")
        self.logger.info(f"Total trips: {total_trips} ")
        self.logger.info(f"Weeks: {weeks} ")
        self.logger.info(f"Weekly Average Number of Trips for {region_name} : {average_trips:.2f}")

