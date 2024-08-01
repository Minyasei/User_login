import requests
import pandas as pd
import mplfinance as mpf
from pandas_datareader import data as pdr
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

crypto_currencies = ["bitcoin", "ethereum", "ripple", "solana", "dogecoin"]

def get_real_time_price(symbol):
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": symbol, "vs_currencies": "usd, try"}
    response = requests.get(url, params=params)
    data = response.json()
    return data[symbol]["usd"]

def get_exchange_rate():
    url = "https://api.exchangeratesapi.io/latest"
    params = {"base": "USD", "symbols": "TRY"}
    response = requests.get(url, params=params)
    data = response.json()
    return data["rates"]["TRY"]  # Correctly access the TRY exchange rate

exchange_rate = get_exchange_rate()

for crypto in crypto_currencies:
    real_time_price_usd = get_real_time_price(crypto)
    real_time_price_try = real_time_price_usd * exchange_rate
    print(f"{crypto.upper()}: ${real_time_price_usd:.2f} | {real_time_price_try:.2f} TRY")

def get_crypto_data(symbol, start_date, end_date):
    df = pdr.DataReader(f'{symbol}-USD', data_source='yahoo', start=start_date, end=end_date)
    return df

crypto_currencies = ["BTC", "ETH", "XRP", "SOL1", "DOGE"]

start_date = (datetime.now() - timedelta(days=1095)).strftime('%Y-%m-%d')
end_date = datetime.now().strftime('%Y-%m-%d')

crypto_data = {}
for crypto in crypto_currencies:
    crypto_data[crypto] = get_crypto_data(crypto, start_date, end_date)

# Charts separately
#fig, axes = mpf.plot(crypto_data, type='candle', title=crypto_currencies, style='yahoo', returnfig=True)
#plt.show()

#print to main screen
print("Real-time Prices:")
for crypto in crypto_currencies:
    real_time_price_usd = get_real_time_price(crypto)
    real_time_price_try = real_time_price_usd * exchange_rate
    print(f"{crypto.upper()}: ${real_time_price_usd:.2f} | {real_time_price_try:.2f} TRY")
plt.show()