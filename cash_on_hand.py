from pathlib import Path 
import csv 
import requests 
my_api = 'VSAFQ7CP9MDL4PCL'
url= 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={my_api}'
 
response= requests.get(url) 
try: 
    import json 
#use .json to retrieve data and stored as JSON object from the API and name it as data_retrieved
    data=response.json() 
    print(json.dumps(data,indent=4)) 

#extract Realtime Currency Exchange Rate from data_retrieved and set it to variable, Realtime_currency_exchange   
    Realtime_currency_exchange = data["Realtime Currency Exchange Rate"] 
#extract data from 5. Exchange Rate from Realtime_currency_exchange and set it to variable,Exchange_Rate
    Exchange_Rate=(float(Realtime_currency_exchange['5. Exchange Rate'])) 
    #print(Exchange_Rate)

    import re 
    from pathlib import Path
    #import csv moduele
    import csv

#assign file path to csv_reports and extend to cash-on-hand-usd.csv
    file_path=Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
#`file_path` is a variable assigned to file after opening it
    with file_path.open(mode = "r",encoding = "UTF-8", newline="") as file:
#use csv.reader to read data in the file
        reader = csv.reader(file) 
#ignore the first row of the data in cash_on_hand_usd.csv
        next(reader)
#create an empty list known as cash_on_hand  
        cash_on_hand=[] 
#create an empty list known as loss_days
        loss_days=[] 
        for values in reader: 
#append values in the csv file into the cash_on_hand
            cash_on_hand.append(values) 
    print(cash_on_hand)
        
#create a variable known as prev_figure and assign float value in cash_on_hand 
    prev_figure=float(cash_on_hand[0][1]) 
#create variable known as day and assign it to cash_on_hand
    day=cash_on_hand 
#create for loop known as current_figure
    for current_figure in cash_on_hand: 
#if current figure is larger than or equal to the prev_figure, assign current_figure to be the prev_figure
        if float(current_figure[1]) >= float(prev_figure): 
            prev_figure=float(current_figure[1]) 
#if current figure is smaller than prev_figure, pre_figure would minus the current_figure to find the difference value
#the difference value would be assign to a variable known as difference  
        else: 
            difference = float(prev_figure) - float(current_figure[1])   
            def convertUSD_SGD(USD):         
                """ 
            -This function will convert USD to SGD by multiplying exchange rate and return the converted value 
            - one parameter required USD (as integer or float) 
            """ 
                return USD * Exchange_Rate 
#create a variable known as SGD and assign the converted amount from USD to SGD into the variable, SGD
            SGD=(convertUSD_SGD(USD=difference)) 
            #print(SGD)
#extract the day in current_figure and set it to a variable known as day
            day=current_figure[0] 
#extract the values in current_figure and set it to a variable known as pre_figure
            prev_figure=float(current_figure[1]) 
            Cash=(f"[CASH DEFICIT] DAY:{day}, AMOUNT:SGD{SGD}")
#append Cash to loss_days
            loss_days.append(Cash) 
            prev_figure=float(current_figure[1]) 
            
    print(loss_days)
except Exception as e:
        print("An error has occured.\nReason:{e}")   