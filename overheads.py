import requests
my_api = 'VSAFQ7CP9MDL4PCL'
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={my_api}'
response = requests.get(url)

import json
data = response.json()
json.dumps(data,indent = 4)

Realtime_currency_exchange = data["Realtime Currency Exchange Rate"]
Exchange_Rate = (float(Realtime_currency_exchange["5. Exchange Rate"]))
print(Exchange_Rate)

import re
from pathlib import Path
# Import csv module
import csv

#assign file path to overheads.csv
file_path = Path.cwd()/"csv_reports"/"overheads.csv"

#create an empty lists known as full_list
full_list=[]
#try:
with file_path.open(mode = "r",encoding = "UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            #print(line)
            full_list.append(line)
print(full_list)
#except Exception as e:
#print(f"An error has occured.\nReason:{e}")
    #create a variable known as highest value and assign it as 0
highest_value = 0

#assign full_list as overheads
overheads = full_list
for current_value in full_list:
# if current value is more than the highest value, current value will be replaced by highest value.
    if float(current_value[1]) > highest_value:
        highest_value = float(current_value[1])
#assign category, overheads, as current value
        overheads = current_value[0]

#create a function, convertUSD_SGD, to convert USD to SGD
def convertUSD_SGD(USD):  
    try:
        """
        -This function will convert USD to SGD by multiplying exchange rate and return the converted value
        - one parameter required USD (as integer or float)
        """
        return USD * Exchange_Rate
    except Exception as e:
        print(f'An error has occurred.\nReason:{e}')
SGD = (convertUSD_SGD(USD=highest_value))
overhead=(f'{overheads} SGD{SGD}')
print(overhead)











        