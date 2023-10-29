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
        path = os.path.dirname(os.path.abspath(__file__))
        create_f = f"{path}/config/sql/{table}.sql"
        query_i = f"{path}/config/sql/etl_{table}.sql"

        # Create table IF NOT EXISTS
        self.logger.info(f'Creating table {table} IF NOT EXISTS')
        create_sql = open(create_f, 'r').read()
        self._execute_query(create_sql)

        # Insert Data after transformation
        self.logger.info(f'Loading {table} table')
        insert_sql = open(query_i, 'r').read()
        self._execute_query(insert_sql, self._file_records, True)

        self.logger.info('ETL completed')

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
