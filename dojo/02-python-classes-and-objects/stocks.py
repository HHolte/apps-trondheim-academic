
# Ticker, Shares, Price
data = [
    ('GOOG', 100, 490.10),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.45),
    ('HPQ', 75, 33.20),
    ('YHOO', 35, 16.35),
    ('SOPPA', 190, 100.00)
]


def cost(stock_data):
    ticker, shares, price = stock_data

    return shares * price
