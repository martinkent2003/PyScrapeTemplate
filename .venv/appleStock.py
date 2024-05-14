import requests
import time
from datetime import datetime

ticker = input("Enter the ticker input: ")

fromDate = input("Enter start date in yyyy/mm/dd format: ")
fd_epoch = int(time.mktime(datetime.strptime(fromDate, '%Y/%m/%d').timetuple()))

toDate = input("Enter end date in yyyy/mm/dd format: ")
td_epoch = int(time.mktime(datetime.strptime(toDate, '%Y/%m/%d').timetuple()))


url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={fd_epoch}&period2={td_epoch}&interval=1d&events=history&includeAdjustedClose=true"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}

content = requests.get(url, headers=headers).content
print(content)
name = ticker+"stock.csv"
with open(name, 'wb') as file :
    file.write(content)