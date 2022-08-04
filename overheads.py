
import requests
my_api = '9UMIAMTHXFT52AUI'
url= 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={my_api}'
response= requests.get(url)

try:
    import json
#use .json to retrieve data and stored as JSON object from the API and name it as data_retrieved
    data_retrieved=response.json()
    json.dumps(data_retrieved,indent=4)

#extract Realtime Currency Exchange Rate from data_retrieved and set it to variable, Realtime_currency_exchange
    Realtime_currency_exchange = data_retrieved["Realtime Currency Exchange Rate"]
#extract data from 5.Exchange rate from Realtime_currency_exchange and set it to variable, Exchange_Rate
    Exchange_Rate=(float(Realtime_currency_exchange["5. Exchange Rate"]))
    #print(Exchange_Rate)

    import re
    from pathlib import Path
    # Import csv module
    import csv

#assign file path to csv_reports and extend to overheads.csv
    file_path = Path.cwd()/"csv_reports"/"overheads.csv"

#create an empty list known as full_list
    full_list=[]
#`file_path` is a variable assigned to file after opening it
    with file_path.open(mode = "r",encoding = "UTF-8", newline="") as file:
#use csv.reader to read data in the file
        reader = csv.reader(file)
#ignore the first row of the data in overheads.csv
        next(reader)
        for line in reader:
            #print(line)
#append line into full_list
            full_list.append(line)
    print(full_list)

#create a variable known as highest value and assign 0 to it
    highest_value = 0
#set full_lists to the variable known overheads
    overheads = full_list
#create a for loop known as current_value
    for current_value in full_list:
#if current value is larger than or equal to the highest value, assign current_value to be the highest value
        if float(current_value[1]) >= highest_value:
            highest_value = float(current_value[1])
#extract the day in current_value and set it to a variable known as overheads
            overheads = current_value[0]
    def convertUSD_SGD(USD):        
        """
        -This function will convert USD to SGD by multiplying the exchange rate and return the converted value
        - one parameter required USD (as integer or float)
        """
        return USD * Exchange_Rate
#create a variable known as SGD and assign the converted amount from USD to SGD into the variable, SGD
    SGD=(convertUSD_SGD(USD=highest_value))
    Overheads = (f"HIGHEST OVERHEADS {overheads}: SGD{SGD}")
    print(Overheads)
except Exception:
        print("An error has occured.")