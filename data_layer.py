import logging
import sqlite3


class DB:
    conn = None
    query = None  # type: str
    query_result = []  # type: list

    logger = logging.getLogger()
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.INFO)

    def __init__(self) -> None:
        self.logger.info("Initialize the class DB")

    def _connection(self, db):
        """" property to connect to the SQLITE
        Returns:
            None
        """
        try:
            self.conn = sqlite3.connect(db)
        except sqlite3.Error as e:
            self.logger.error(f"Error connecting to SQLITE, Error: {e}")
            raise Exception(f"Error to connect to SQLITE, Error: {e}")

    def _execute_query(self, query: str, parameter=None, is_execute_many: bool = False) -> list:
        """Cursor process to execute SQL statements)
        Raises:
            Exception: An error has occurred during the SQL execution
        Returns:
            None
        """
        if parameter is None:
            parameter = []
        conn = self.conn
        try:
            with conn:
                cursor = conn.cursor()
                if is_execute_many:
                    cursor.executemany(query, parameter)
                else:
                    cursor.execute(query, parameter)
                    cursor.fetchall()

        except Exception as e:
            self.logger.error(f"Execution query Error: {e}")

    def close_connection(self):
        """
        Close SLITE connection to SQL Server
        """
        self.conn.commit()
        self.conn.close()
