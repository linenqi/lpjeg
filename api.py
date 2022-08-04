import requests
my_api = 'VSAFQ7CP9MDL4PCL'
url= 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={my_api}'
response= requests.get(url)
print(response)

import json
data=response.json()
print(json.dumps(data,indent=4))

