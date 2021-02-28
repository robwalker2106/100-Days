import requests
from datetime import date, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_api = "https://www.alphavantage.co/query"
stock_key = "KEY"

stock_params= {'apikey': stock_key,
               'function': 'TIME_SERIES_DAILY_ADJUSTED',
               'symbol': STOCK}

response = requests.get(stock_api, params=stock_params)
response.raise_for_status()
stock_data = response.json()['Time Series (Daily)']


day_one = date.today()

if day_one.weekday() == 6:
    day_one = day_one - timedelta(days=2)
elif day_one.weekday() == 0:
    day_one = day_one - timedelta(days=3)
else:
    day_one = day_one - timedelta(days=1)

day_two = day_one - timedelta(days=1)

if day_one.weekday() == 0:
    day_two = day_one - timedelta(days=3)

day_one_close = float(stock_data[str(day_one)]['4. close'])
day_two_close = float(stock_data[str(day_two)]['4. close'])

pct_change = (day_one_close - day_two_close) / day_one_close

if abs(pct_change) >= .05:
    print("Get News")
else:
    print("Slow day")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

