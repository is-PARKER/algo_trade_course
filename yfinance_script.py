import yfinance as yf
import pandas as pd

data = yf.download('MSFT', start='2023-01-01', end='2023-12-31', interval="1" )

print(data)