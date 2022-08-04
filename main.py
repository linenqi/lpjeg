import cash_on_hand
import overheads
import profit_loss
import api

from pathlib import Path
#assign file path to summary_report.txt
file_path = Path.cwd()/"summary_report.txt"
#create file path
file_path.touch()
#print(file_path.exists)

#`file_path` is a variable assigned to file after opening it
with file_path.open(mode='a',encoding='UTF-8',newline='') as file :
    file.write(f'[REAL TIME CURRENCY CONVERSION RATE] USD1= SGD{api.Exchange_Rate}')
    file.write('\n')
    file.write(f'{overheads.Overheads}')
    file.write('\n')
    file.write(f" {cash_on_hand.loss_days[0]}")
    file.write('\n')
    file.write(f'{cash_on_hand.loss_days[1]}')
    file.write('\n')
    file.write(f'{cash_on_hand.loss_days[2]}')
    file.write('\n')
    file.write(f'{profit_loss.profitloss[0]}')
    file.write('\n')
    file.write(f'{profit_loss.profitloss[1]}')
    file.write('\n')
    file.write(f'{profit_loss.profitloss[2]}')
    file.write('\n')
    file.write(f'{profit_loss.profitloss[3]}')
    file.write('\n')
    file.write(f'{profit_loss.profitloss[4]}')
