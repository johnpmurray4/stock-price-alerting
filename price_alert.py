import os.path
import yfinance as yf
import pandas as pd
import smtplib
import configparser


def main():
    with open(os.path.dirname(__file__) + '/data/tickers_to_check.csv') as f:
        lines = f.readlines()

    check_prices(lines)


def check_prices(tickersToCheck):
    for line in tickersToCheck:
        ticker, stopLoss, target = line.split(",", 3)
        print("Checking price for %s, stop loss is %s, with target %s" %
              (ticker, stopLoss, target))

        price = get_price(ticker)
        print("Price for ticker %s is %s" % (ticker, str(price)))

        if (price < float(stopLoss)):
            print("Price is lower than stop loss")
            send_email("Stop loss hit", ticker, price, float(stopLoss))

        if (price > float(target)):
            print("Price is higher than target")
            send_email("Target met", ticker, price, float(target))


def get_price(ticker: str) -> float:
    ticker_yahoo = yf.Ticker(ticker)
    data = ticker_yahoo.history()
    return float(data.tail(1).iloc[0]['Close'])


def send_email(action: str, ticker: str, currentPrice: float, targetPrice: float):
    print("Sending email alert")
    config = configparser.RawConfigParser()
    config.read('properties.config')

    gmail_user = config.get('EMAIL_CREDENTIALS', 'username')
    gmail_password = config.get('EMAIL_CREDENTIALS', 'password')

    sent_from = gmail_user
    to = [config.get('EMAIL_RECIPIENT', 'recipient')]
    subject = action
    body = "Current price for ticker %s is %s - alert at %s" % (
        ticker, str(currentPrice), str(targetPrice))

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (sent_from, ", ".join(to), subject, body)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, message)
    server.close()


if __name__ == "__main__":
    main()
