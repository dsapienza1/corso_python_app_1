from time import sleep
import pandas as pd


def process_data(data):
    print("Beginning data processing...")
    sleep(3)
    print("Data processing finished.")
    return data

def read_data_from_web(data_url, nrows):
    print("Reading data from the Web")
    data = pd.read_csv(data_url, nrows=nrows)
    print(data.head())
    return data

def write_data_to_target(data, target_file):
    print("Writing data the output folder")
    data.to_excel(target_file, index=False)
    print(data)
