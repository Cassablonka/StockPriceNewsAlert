# StockPriceNewsAlert
This project keeps the track of Stock Price of certain stock and gives alert in the form of SMS if major any stock related news break out.

In this project 3 APIs has been used.

1. https://www.alphavantage.co/ for Stocks Data
2. https://newsapi.org/ for News Data
3. https://www.twilio.com/ for Messaging

The company on watch is Tesla Incorporation.

Whenever Tesla losses or gains share value which is greater or smaller than 5%, the SMS API triggers and send us a alert message. ( See image for reference. )
This message contains Headline, its Breif and related Link for the News Article due to which the stock may have been affected.

The Messaging API send us 3 top news related to our stock on watch.

This is a major usecase for people who dont want to contantly check on their investment and get notified only when major changes happens.
