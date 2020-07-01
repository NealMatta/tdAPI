import requests
from config import consumer_key

# Daily Prices Endpoint


# Price History
stock = "GOOG"
endpoint = "https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format(
    stock.upper())
payload = {'apikey': consumer_key,
           'period': '2',
           'periodType': 'day',
           'frequencyType': 'minute',
           'frequency': '1',
           'startDate': '1593561600',
           'needExtendedHoursData': 'false',
           }

# content = requests.get(url=endpoint, params=payload)
# data = content.json()

# Get Quote

stock = "ES"
endpoint = "https://api.tdameritrade.com/v1/marketdata/{}/quotes".format(
    stock.upper())

payload = {'apikey': consumer_key, }


content = requests.get(url=endpoint, params=payload)
data = content.json()
print(data)
