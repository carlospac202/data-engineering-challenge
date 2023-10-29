from etl_process import EtlProcess
from analytics import Analytics

def main():
    # Create instances of your classes
    etl = EtlProcess()
    analytics = Analytics()

    # Call methods from lassA
    etl.process()
    analytics.group_data()

if __name__ == "__main__":
    main()  # Call the main function when the script is executed
