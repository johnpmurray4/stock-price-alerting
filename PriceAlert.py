import os.path
import yfinance as yf
import pandas as pd


def main():
    with open(os.path.dirname(__file__) + '/data/stocks.csv') as f:
        lines = f.readlines()

    checkPrices(lines)


def checkPrices(tickersToCheck):
    for line in tickersToCheck:
        ticker, stopLoss, target = line.split(",", 3)
        print("Checking price for " +
              ticker + ", stop loss is " + stopLoss + ", with target " + target)

        price = getPrice(ticker)
        print("Price for ticker " + ticker + " is " + str(price))

        if (price < float(stopLoss)):
            print("Price is lower than stop loss")
            sendEmail("STOP", price, float(stopLoss))

        if (price > float(target)):
            print("Price is higher than target")
            sendEmail("TARGET_MET", price, float(target))


def getPrice(ticker: str) -> float:
    ticker_yahoo = yf.Ticker(ticker)
    data = ticker_yahoo.history()
    return float(data.tail(1).iloc[0]['Close'])


def sendEmail(action: str, currentPrice: float, targetPrice: float):
    print("Sending email alert")


if __name__ == "__main__":
    main()
