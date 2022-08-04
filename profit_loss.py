from pathlib import Path  
import csv  
import requests  
my_api = '9UMIAMTHXFT52AUI' 
url= 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={my_api}' 
 
response = requests.get(url) 
#print(response) 

try: 
    import json 
#use .json to retrieve data and stored as JSON object from the API and name it as data_retrieved 
    data_retrieved=response.json()  
    print(json.dumps(data_retrieved,indent=4))  

#extract Realtime Currency Exchange Rate from data_retrieved and set it to variable, Realtime_currency_exchange
    Real_Time_Currency_Rate =data_retrieved["Realtime Currency Exchange Rate"]  
#extract data from 5.Exchange rate from Realtime_currency_exchange and set it to variable, Exchange_Rate
    ExchangeRate=(float(Real_Time_Currency_Rate['5. Exchange Rate'])) 
    #print(Exchange_Rate)

    import re
    from pathlib import Path
    # Import csv module
    import csv

#assign file path to csv_reports and extend to profit-and-loss-usd.csv
    file_path=Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv" 
#`file_path` is a variable assigned to file after opening it 
    with file_path.open(mode = "r",encoding = "UTF-8", newline="") as file:  
#use csv.reader to read data in the file
        reader = csv.reader(file) 
#ignore the first row of the data in profit-and-loss-usd.csv 
        next(reader)  
#create empty list known as profitloss
        profitloss=[]  
#create empty list known as pnldata
        pnldata=[]  
        for value in reader:  
#append value into pnldata
            pnldata.append(value)  
#create a variable known as prev_value and assign float value in pnldata   
    prev_value=float(pnldata[0][4])
#create a variable known as day and assign it to pnldata 
    day=pnldata 
#crate a for loop known as current_value 
    for currentvalue in pnldata:  
#if current value is larger than or equal to the prev_value, assign current_value to be the prev_value
        if float(currentvalue[4]) >= float(prev_value):  
            prev_value=float(currentvalue[4])  
#if current value is smaller than prev_value, pre_value would minus the current_value to find the difference value
#the difference value would be assign to a variable known as difference  
        else:  
            difference =  float(prev_value) - float(currentvalue[4])    
            def convertUSD_SGD(USD):          
                """  
            -This function will convert USD to SGD by multiplying exchange rate and the USD and return the converted value  
            - one parameter required USD (as integer or float)  
            """  
                return USD * ExchangeRate  
#create a variable known as SGD and assign the converted amount from USD to SGD into the variable, SGD
            SGD=(convertUSD_SGD(USD=difference))  
#extract the day in current_value and set it to a variable known as day
            day=currentvalue[0] 
#extract the values in current_value and set it to a variable known as pre_value
            prev_value=float(currentvalue[4]) 
            ProfitnLoss=(f"[PROFIT DEFICIT] DAY:{day} AMOUNT:SGD{SGD}")
            profitloss.append(ProfitnLoss)  
            prev_value=float(currentvalue[4])
    
    print(profitloss)
except Exception:
        print("An error has occured.")
