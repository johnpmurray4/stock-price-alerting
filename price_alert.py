import os.path
import yfinance as yf
import pandas as pd


def main():
    with open(os.path.dirname(__file__) + '/data/tickers_to_check.csv') as f:
        lines = f.readlines()

    check_prices(lines)


def check_prices(tickersToCheck):
    for line in tickersToCheck:
        ticker, stopLoss, target = line.split(",", 3)
        print("Checking price for " +
              ticker + ", stop loss is " + stopLoss + ", with target " + target)

        price = get_price(ticker)
        print("Price for ticker " + ticker + " is " + str(price))

        if (price < float(stopLoss)):
            print("Price is lower than stop loss")
            send_email("STOP", price, float(stopLoss))

        if (price > float(target)):
            print("Price is higher than target")
            send_email("TARGET_MET", price, float(target))


def get_price(ticker: str) -> float:
    ticker_yahoo = yf.Ticker(ticker)
    data = ticker_yahoo.history()
    return float(data.tail(1).iloc[0]['Close'])


def send_email(action: str, currentPrice: float, targetPrice: float):
    print("Sending email alert")


if __name__ == "__main__":
    main()
