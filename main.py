# Import the required packages
import requests
from twilio.rest import Client

# Websites to use
# 1. Use https://www.alphavantage.co/ for Stocks Data
# 2. Use https://newsapi.org/ for News Data
# 3. Use https://www.twilio.com/ for Messaging

# Setting the API end points
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Define all the required variables
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "Your Stock Api Key"
NEWS_API_KEY = "Your News Api Key"
TWILIO_SID = "Your Twilio SID"
TWILIO_AUTH_TOKEN = "Your Twilio Auth Token"

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_api_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_api_parameters)
data = response.json()['Time Series (Daily)']
price_list = [value for (key, value) in data.items()]
yesterdays_price = float(price_list[0]['4. close'])

# Get the day before yesterday's closing stock price

day_before_yesterdays_price = float(price_list[1]['4. close'])

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

diff = round(abs(yesterdays_price - day_before_yesterdays_price), 2)

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percent_diff = round((diff / yesterdays_price) * 100, 2)

# Use the News API to get articles related to the COMPANY_NAME.

if percent_diff > 5:
    news_api_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

# Create a new list of the first 3 article's headline and description using list comprehension.

response = requests.get(NEWS_ENDPOINT, params=news_api_params)
articles = response.json()['articles'][:3]


formatted_articles = [
    f'{COMPANY_NAME}: 📈{percent_diff}%\nHeadline: {article["title"]}. \nBrief: {article["description"]}. \nURL: {article["url"]}'
    for article in articles]

# Send each article as a separate message via Twilio.

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

for article in formatted_articles:
    message = client.messages \
        .create(
        body=article,
        from_='Random Generated Number from Twilio',
        to='Your Phone Number'
    )
    print("SMS successfully sent.")