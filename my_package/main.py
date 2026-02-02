from time import sleep
import pandas as pd
import os
from dotenv import load_dotenv
import logging

from utils import read_data_from_web, process_data, write_data_to_target



def main():

    logging.basicConfig(
        filename="log/app.log",  
        level=logging.INFO,  # livello minimo di log
        format="%(asctime)s - %(levelname)s - %(message)s")
    
    logging.info("Applicazione avviata")
    load_dotenv()  # carica il file .env

    DATA_URL = os.getenv("DATA_URL")
    OUTPUT_FILE = os.getenv("OUTPUT_FILE")

    #print(f"DATA_URL: {DATA_URL}")
    #print(f"OUTPUT_FILE: {OUTPUT_FILE}")
    logging.info(f"DATA_URL: {DATA_URL}")
    logging.info(f"OUTPUT_FILE: {OUTPUT_FILE}")

    data = read_data_from_web(DATA_URL, 100)
    modified_data = process_data(data)
    write_data_to_target(modified_data, OUTPUT_FILE)

    logging.info("Applicazione completata")
if __name__ == "__main__":
    main()

