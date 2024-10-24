# Import necessary libraries
import yfinance as yf

# Extract stock data
ticker = 'TSLA'
period = '5y'
interval = '1d'

df = yf.download(ticker, period=period, interval=interval)
