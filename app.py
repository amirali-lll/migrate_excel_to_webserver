import pandas as pd 
import requests
import logging
import sys


logging.basicConfig(filename='requests.log', level=logging.INFO, format='%(asctime)s - %(message)s')

logging.info("reading excel file...")
excel_file = "accounts2.xlsx"
df = pd.read_excel(excel_file, dtype={'ssn': str}) 

total_rows = len(df)




logging.info("iterating rows...")

for index, row in df.iterrows():
    print(f"{index+1}/{total_rows}")
    ssn = str(row['ssn']) 
    travel_debit = int(row['travel_debit'])
    travel_credit = int(row['travel_credit'])  
    
    
    # check the ssn lenght
    # if (ssn.__len__()!=10):
    #     logging.info(f"{index+1}| {ssn} || {travel_debit} || {travel_credit}")


    data = {
        "ssnUsers": [
            ssn
        ],
        "segmentType":"Trip",
        "debitAmount":travel_debit,
        "creditAmount":travel_credit
    }
    print(f"request the server with data:{data}")
    response = requests.post("https://api-test.basa.ir/v1/payGate/createSegment",json=data)    
    if response.status_code == 200:
        print(f"Request successful for SSN: {ssn}")
    else:
        error_message = f"Failed to make request for SSN: {ssn}. Status code: {response.status_code}. message: {response.content}"
        print(error_message)
        logging.error(error_message)
