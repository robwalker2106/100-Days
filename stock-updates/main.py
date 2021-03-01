import requests
from datetime import date, timedelta
from newsapi import NewsApiClient
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_KEY = "KEY"
TWILIO_SID = 'AC77dc6aa70731198115a4c4c02afd275f'
TWILIO_AUTH_TOKEN = 'KEY'

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)


def send_article(dic):
    info = f"{STOCK}:  {change}{round(pct_change * 100, 0)}\nHeadline: {dic['title']}\nBrief: {dic['description']}\n" \
            f"{dic['url']}"
    message = client.messages \
        .create(
        body=info,
        from_='+15139861124',
        to='NUMBER')


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


