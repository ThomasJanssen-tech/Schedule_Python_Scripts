import requests
import json
import datetime
import pandas as pd

current_time = datetime.datetime.now()

page = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

data = json.loads(page.text)

price = data['bpi']['USD']['rate_float']

data = {'date':  [current_time],
        'sales': [price],
        }

df = pd.DataFrame(data)

df.to_csv("btc_price.csv", mode="a", index=False, header=False)