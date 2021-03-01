import requests
from datetime import date, timedelta
from newsapi import NewsApiClient
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_KEY = "key"
TWILIO_SID = 'AC77dc6aa70731198115a4c4c02afd275f'
TWILIO_AUTH_TOKEN = 'key'

client = Client(account_sid, auth_token)


def send_article(dic):
    info = f"{STOCK}:  {change}{round(pct_change * 100, 0)}\nHeadline: {dic['title']}\nBrief: {dic['description']}\n" \
            f"{dic['url']}"
    message = client.messages \
        .create(
        body=info,
        from_='+15139861124',
        to='number')

    print(info)


def get_news():
    newsapi = NewsApiClient(api_key=NEWS_KEY)

    all_data = newsapi.get_everything(q=COMPANY_NAME,
                                          from_param=day_two,
                                          to=date.today(),
                                          language='en',
                                          sort_by='relevancy')
    all_articles = all_data['articles']

    if len(all_articles) >= 3:
        return all_articles[:3]
    else:
        return all_articles[:len(all_articles)]


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_api = "https://www.alphavantage.co/query"
stock_key = "key"

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
#pct_change = - 0.075
change = ""
if pct_change > 0:
    change = "🔺"
else:
    change = "🔻"

news_data = {}
if abs(pct_change) >= .05:
    news_data = get_news()
else:
    print(f"{STOCK}:  {change}{round(pct_change * 100, 0)}")

if len(news_data) > 0:
    for article in news_data:
        send_article(article)


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

