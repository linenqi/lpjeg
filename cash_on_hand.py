from pathlib import Path 
import csv 
import requests 
my_api = 'VSAFQ7CP9MDL4PCL'
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={my_api}'
 
response = requests.get(url) 
 
import json 
try:
    data = response.json() 
    print(json.dumps(data,indent=4))
except Exception as e:
        print("An error has occured.\nReason:{e}")

data = response.json() 
json.dumps(data,indent=4)

 
Realtime_currency_exchange = data["Realtime Currency Exchange Rate"] 
Exchange_Rate = (float(Realtime_currency_exchange['5. Exchange Rate'])) 
#print(Exchange_Rate)

import re 
from pathlib import Path
#import csv moduele
import csv 
file_path = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
try :
    with file_path.open(mode = "r",encoding = "UTF-8", newline="") as file: 
        reader = csv.reader(file) 
        next(reader) 
except Exception as e:
    print("An error has occured.\nReason:{e}")

    cash_on_hand = [] 
    loss_days = [] 
    for values in reader: 
        cash_on_hand.append(values) 
     
 
prev_figure = float(cash_on_hand[0][1]) 
day = cash_on_hand 
for current_figure in cash_on_hand: 
    if float(current_figure[1]) >= float(prev_figure): 
        prev_figure = float(current_figure[1])  #replace prev with curr 
    else: 
        difference = float(prev_figure) - float(current_figure[1])   
def convertUSD_SGD(USD):  
    try:           
        """ 
        -This function will convert USD to SGD by multiplying exchange rate and return the converted value 
        - one parameter required USD (as integer or float) 
        """ 
        return USD * Exchange_Rate 
    except Exception as e:
        print(f"An error has occured.\nReason:{e}")
  
        SGD = (convertUSD_SGD(USD = difference)) 

        day = current_figure[0] 
        prev_figure = float(current_figure[1]) 
        Cash = (day,SGD) 
        loss_days.append(Cash) 
        prev_figure = float(current_figure[1]) 
        
print(loss_days)