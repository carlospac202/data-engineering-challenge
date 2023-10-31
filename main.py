import sys
import os
from etl_process import EtlProcess
from analytics import WeekData

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


def main():
    # Create instances
    etl = EtlProcess()

    # Call methods from class
    etl.process()

    data = WeekData(etl.result)
    data._data_calculations()

if __name__ == "__main__":
    main()  # Call the main function when the script is executed
