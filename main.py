import cash_on_hand
import overheads
import profit_loss
import api

from pathlib import Path
#assign file path to summary_report.txt
file_path = Path.cwd()/"summary_report.txt"
#create file path
#file_path.touch()
#print(file_path.exists)
with file_path.open(mode='a', encoding='UTF-8') as file:
    file.writelines(overheads.Overhead_value)




