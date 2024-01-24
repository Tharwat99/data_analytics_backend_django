import csv
from .models import Data

def handle_csv_file(file):
    reader = csv.DictReader(file.read().decode('utf-8').splitlines())
    data_list =[Data(month = row['Month'],revenue =row['Revenue'],expenses = row['Expenses'],profit = row['Profit']) for row in reader]
    return data_list