from pathlib import Path  
import csv  
import requests  
my_api = 'VSAFQ7CP9MDL4PCL' 
url= 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={my_api}' 
 
response = requests.get(url) 
print(response) 
 
import json  
<<<<<<< HEAD
try:
    data = response.json()  
    print(json.dumps(data,indent=4))  
except Exception as e:
        print("An error has occured.\nReason:{e}")

=======
<<<<<<< HEAD
data=response.json()  
json.dumps(data,indent=4)
=======
data = response.json()  
print(json.dumps(data,indent=4))  
>>>>>>> 670cfb597fd1acf8e6061e4fc50439830d0a609e
>>>>>>> bac2cb6e72de42041a7a94cd4966446fe8af193f
  
Real_Time_Currency_Rate = data["Realtime Currency Exchange Rate"]  
ExchangeRate = (float(Real_Time_Currency_Rate['5. Exchange Rate'])) 
 
file_path = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv" 

try:
    with file_path.open(mode = "r",encoding = "UTF-8", newline="") as file:  
        reader = csv.reader(file)  
        next(reader) 
except Exception as e:
        print("An error has occured.\nReason:{e}")
        profitloss = []  
        pnldata = []  
        for value in reader:  
            pnldata.append(value)  
      
prev_value = float(pnldata[0][4])  
day = pnldata 
for currentvalue in pnldata:
    if float(currentvalue[4]) >= float(prev_value):  
        prev_value = float(currentvalue[4])    
    else:  
        difference =  float(prev_value) - float(currentvalue[4])    
        def convertUSD_SGD(USD):
        try:          
            """  
            -This function will convert USD to SGD by multiplying exchange rate and the USD and return the converted value  
            - one parameter required USD (as integer or float)  
            """  
                return USD * ExchangeRate 
        except Exception as e:
                print("An error has occured.\nReason:{e}")
 
        SGD = (convertUSD_SGD(USD=difference))  
 
        day = currentvalue[0]  
        prev_value = float(currentvalue[4])  
        ProfitnLoss = (day,SGD)  
        profitloss.append(ProfitnLoss)  
        prev_value = float(currentvalue[4])  
 
print(profitloss)