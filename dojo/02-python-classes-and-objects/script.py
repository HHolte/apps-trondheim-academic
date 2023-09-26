import stocks

def main(data):
    for ticker, shares, price in data:
        stock_data = ticker, shares, price
        cost = stocks.cost(stock_data)
        print(f"{ticker} {shares} {price} - total: {cost}")

if __name__ == "__main__":
    main(stocks.data)

