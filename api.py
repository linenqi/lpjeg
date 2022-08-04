import requests
from pathlib import Path
my_api = '9UMIAMTHXFT52AUI'
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={my_api}'
response = requests.get(url)
print(response)

import json
data = response.json()
print(json.dumps(data,indent=4))
#extract Realtime Currency Exchange Rate from data_retrieved and set it to variable, Realtime_currency_exchange   
Realtime_currency_exchange = data["Realtime Currency Exchange Rate"] 
#extract data from 5. Exchange Rate from Realtime_currency_exchange and set it to variable,Exchange_Rate
Exchange_Rate=(float(Realtime_currency_exchange['5. Exchange Rate'])) 
print(Exchange_Rate)
    
