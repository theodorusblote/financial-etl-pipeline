# Import necessary libraries
import yfinance as yf
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

# Extract
# Set parameters
ticker = 'TSLA'
period = '5y'
interval = '1d'

# Download stock data
df = yf.download(ticker, period=period, interval=interval)

# Transform
# Reset index
df.reset_index(inplace=True)

# Add features
# 50-Day SMA
df['50-Day SMA'] = df['Adj Close'].rolling(window=50).mean()

# 200-Day SMA
df['200-Day SMA'] = df['Adj Close'].rolling(window=200).mean()

# Lag open
df['Lag Open'] = df['Open'].shift(1)

# Lag volume
df['Lag Volume'] = df['Volume'].shift(1)

# RSI
def RSI(df, window=14):
    change = df['Adj Close'].diff()
    gain = change.where(change > 0, 0)
    loss = -change.where(change < 0, 0)
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()
    RS = avg_gain / avg_loss
    RSI = 100 - (100 / (1 + RS))

    return RSI

df['RSI'] = RSI(df)

# Daily return
df['Daily Return'] = df['Adj Close'].pct_change()

# Lag daily return
df['Lag Daily Return'] = df['Daily Return'].shift(1)

# Drop NaN values resulting from calculations
df.dropna(inplace=True)

# Load
# Load environment variables
load_dotenv()

DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# Create SQL engine
engine = create_engine(f'postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Load DataFrame into SQL database
df.to_sql('stock_data', con=engine, if_exists='replace', index=False)
