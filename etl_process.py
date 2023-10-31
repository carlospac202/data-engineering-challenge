import pandas as pd
import os
from config import Config


class EtlProcess(Config):
    _file_records = []  # type: list
    def __init__(self):
        """
        Constructor
        """
        self.config()

    def _read_data(self) -> pd.DataFrame:
        file = self._yaml_config.get('input_file')
        return pd.read_csv(file).fillna('')

    def _transform_data(self, df):
        for index, row in df.iterrows():
            region = row['region']
            origin_coord = row['origin_coord']
            destination_coord = row['destination_coord']
            datetime = row['datetime']
            datasource = row['datasource']

            # Extract latitude and longitude from origin and destination coordinates
            origin_lat, origin_lon = map(float, origin_coord.strip('POINT ()').split())
            destination_lat, destination_lon = map(float, destination_coord.strip('POINT ()').split())

            self._file_records.append(
                [region, origin_lat, origin_lon, destination_lat, destination_lon, datetime, datasource])

    def _load_data(self):
        """
        Method in charge of processing the rows of the files and inserting them into the database table
        """
        # Open connection to SQLITE with specific database provided in config.yml
        self._connection(self._yaml_config.get('database'))

        # Set up variables
        table = self._yaml_config.get('table')
        current_dir = os.path.dirname(os.path.abspath(__file__))
        #create_f = os.path.join(current_dir, f"../sql/{table}.sql")
        create_f = os.path.join(current_dir, f"sql/{table}.sql")
        #query_i = os.path.join(current_dir, f"../sql/etl_{table}.sql")
        query_i = os.path.join(current_dir, f"sql/etl_{table}.sql")

        # Create table IF NOT EXISTS
        self.logger.info(f'Creating table {table} IF NOT EXISTS')
        create_sql = open(create_f, 'r').read()
        self._execute_query(create_sql)

        # Insert Data after transformation
        self.logger.info(f'Loading {table} table')
        insert_sql = open(query_i, 'r').read()
        self._execute_query(insert_sql, self._file_records, True)

        self.logger.info('ETL completed')
        self.logger.info(f'Inserted into table {table} {"{:,}".format(len(self._file_records))} records')

    def _group_data(self):
        """
        Method in charge of grouping Trips with similar origin, destination, and time of day.
        """
        query = f"""
        CREATE TABLE IF NOT EXISTS trips_grouped 
        AS 
            SELECT
                  region,
                  origin_lat,
                  origin_lon,
                  destination_lat,
                  destination_lon,
                  CAST(datetime AS TIME) AS time_of_day,
                  COUNT(*) AS trip_count
            FROM trips
            GROUP BY region, origin_lat, origin_lon, destination_lat, destination_lon, CAST(datetime AS TIME)
            HAVING COUNT(*) > 1
            ORDER BY COUNT(*) DESC;
            """

        self._execute_query(query)
        self.logger.info(f"New table trips_grouped created")


    def _weekly_process(self):

        region_name = 'Turin'

        # Write the SQL query to calculate the weekly average by region
        query = f"""
            SELECT strftime('%Y-%W', datetime) AS week, COUNT(*) AS trip_count
            FROM trips
            WHERE region = ?
            GROUP BY week
            """

        self.result = self._execute_query(query, (region_name,))

    def process(self) -> None:
        """
        Public method to execute the ETL, this method does nothing and returns
        """
        # Read process
        data_frame = self._read_data()

        # Transform process
        self._transform_data(data_frame)

        # Load process
        self._load_data()

        # Group data
        self._group_data()

        # Weekly process
        self._weekly_process()
