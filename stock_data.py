import yfinance as yf
import pandas as pd
import os

def get_stock_data(ticker: str, period: str = "1y"):
    try:
        data = yf.download(ticker, period=period)
        return pd.DataFrame(data)
    except Exception as e:
        print(f"Error downloading data for {ticker}: {e}")
        return None

def save_to_csv(df: pd.DataFrame, filename: str):
    if df is None:
        return
    try:
        os.makedirs("data", exist_ok=True)
        filepath = os.path.join("data", filename)
        df.to_csv(filepath, index=True)
        print(f"Stock data saved to {filepath}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def get_daily_prices(ticker: str, period: str = "1y"):
    df = get_stock_data(ticker, period)
    if df is not None:
        daily_prices = df['Close']
        return daily_prices
    return None

def save_daily_prices_to_csv(daily_prices: pd.Series, filename: str):
    if daily_prices is None:
        return
    try:
        os.makedirs('data', exist_ok=True)
        filepath = os.path.join('data', filename)
        daily_prices.to_csv(filepath, header=True)
        print(f"Daily prices saved to: {filepath}")
    except Exception as e:
        print(f"Error saving daily prices to CSV: {e}")

def main():
    ticker = "AAPL"
    period = "1y"
    df = get_stock_data(ticker, period)
    if df is not None:
        save_to_csv(df, f"{ticker}_data.csv")
        daily_prices = get_daily_prices(ticker, period)
        if daily_prices is not None:
            save_daily_prices_to_csv(daily_prices, f"{ticker}_daily_prices.csv")
            print(f"\nDaily Closing Prices for {ticker} ({period}):")
            print(daily_prices.head())

if _name_ == "_main_":
    main()