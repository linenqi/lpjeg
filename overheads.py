
import requests
my_api = 'VSAFQ7CP9MDL4PCL'
url= 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={my_api}'
response= requests.get(url)

try:
    import json
#use .json to retrieve data and stored as JSON object from the API and name it as data_retrieved.
    data_retrieved=response.json()
    json.dumps(data_retrieved,indent=4)

#extract Realtime Currency Exchange Rate from data_retrieved and set it to variable, Realtime_currency_exchange.
    Realtime_currency_exchange = data_retrieved["Realtime Currency Exchange Rate"]
#extract data from exchange rate 
    Exchange_Rate=(float(Realtime_currency_exchange["5. Exchange Rate"]))
    print(Exchange_Rate)

    import re
    from pathlib import Path
    # Import csv module
    import csv

    file_path = Path.cwd()/"csv_reports"/"overheads.csv"

    full_list=[]
    with file_path.open(mode = "r",encoding = "UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            #print(line)
            full_list.append(line)
    print(full_list)

    highest_value = 0
    overheads = full_list
    for current_value in full_list:
        if float(current_value[1]) > highest_value:
            highest_value = float(current_value[1])
            overheads = current_value[0]
    def convertUSD_SGD(USD):        
        """
        -This function will convert USD to SGD by multiplying exchange rate and return the converted value
        - one parameter required USD (as integer or float)
        """
        return USD * Exchange_Rate
    SGD=(convertUSD_SGD(USD=highest_value))


    print(overheads, SGD)
except Exception as e:
        print("An error has occured.\nReason:{e}")