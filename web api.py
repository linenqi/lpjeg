import requests
my_api = 'VSAFQ7CP9MDL4PCL'
url= 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={my_api}'
response= requests.get(url)

import json
data=response.json()
print(json.dumps(data,indent=4))

close_data=data["Realtime Currency Exchange Rate"]
Exchange_Rate=(float(close_data['5. Exchange Rate']))
print(Exchange_Rate)