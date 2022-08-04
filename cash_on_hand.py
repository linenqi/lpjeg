from pathlib import Path 
import csv 
import requests 
my_api = 'VSAFQ7CP9MDL4PCL'
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={my_api}'
 
response = requests.get(url)
#use .json to retrieve data and stored as JSON object from the API and name it as data_retrieved
try: 
    import json 
    data = response.json() 
    print(json.dumps(data,indent = 4)) 

    #extract Realtime Currency Exchange Rate from data_retrieved and set it to variable, Realtime_currency_exchange
    Realtime_currency_exchange = data["Realtime Currency Exchange Rate"] 
    #extract 5. Exchange Rate from Realtime_currency_exchange and set it to variable,Exchange_Rate
    Exchange_Rate = (float(Realtime_currency_exchange['5. Exchange Rate'])) 
    print(Exchange_Rate)

    import re 
    from pathlib import Path
    #import csv moduele
    import csv 
    #assign file path to csv_reports and extend to cash-on-hand-usd.csv
    file_path = Path.cwd()/"csv_reports"/"cash_on_hand-usd.csv"

    with file_path.open(mode = "r",encoding = "UTF-8", newline="") as file: 
        #use csv.reader to read data in the file
        reader = csv.reader(file) 
        #ignore the first row of the data in cash_on_hand_usd.csv
        next(reader) 
        #create an empty list and name it cash_on_hand 
        cash_on_hand = [] 
        #create an flag list and name it loss_days
        loss_days = [] 
        for values in reader: 
            #Append the rest of the values in the csv file into the cash_on_hand
            cash_on_hand.append(values) 
        
    #Make cash on hand value as float and set them to pre_figures
    prev_figure = float(cash_on_hand[0][1]) 
    #Create variable for cash_on_hand values and then name them as day 
    day = cash_on_hand 
    #Creating for loop and name values in cash_on_hand as value
    for current_figure in cash_on_hand: 
        #if the current_figure is larger or equals to prev_figure the current_figure will be replaced by the pre_figure
        if float(current_figure[1]) >= float(prev_figure): 
            prev_figure = float(current_figure[1])  
        else: 
            difference = float(prev_figure) - float(current_figure[1])   
            def convertUSD_SGD(USD):         
                """ 
            -This function will convert USD to SGD by multiplying exchange rate and return the converted value 
            - one parameter required USD (as integer or float) 
            """ 
                return USD * Exchange_Rate 
                #create a variable known as SGD and assign the converted amount from USD to SGD into the variable, SGD
            SGD = (convertUSD_SGD(USD = difference)) 
            print(SGD)
            #set the first value in current_figure as day
            day = current_figure[0] 
            #make the current cash_on_hand value as float and set as new pre_figure
            prev_figure = float(current_figure[1]) 
            #set day and cash_on_hand value as Cash
            Cash = (f"[CASH DEFICIT DAY:{day}, AMOUNT:{SGD}")
            #append the cash_on_hand value into loss_days
            loss_days.append(Cash)
            prev_figure = float(current_figure[1])
            
    print(loss_days)
except Exception as e:
        print("An error has occured.\nReason:{e}")
        
