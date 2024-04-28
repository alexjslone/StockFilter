#from chatgpt
#test
import yfinance as yf
import matplotlib.pyplot as plt

def fetch_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

def filter_stock_data(stock_data, percentage_drop_threshold):
    last_year_data = stock_data['Adj Close'].pct_change(252) * 100
    filtered_stocks = last_year_data[last_year_data <= -percentage_drop_threshold]
    return filtered_stocks

def visualize_stocks(stock_data):
    stock_data.plot(y='Adj Close', title='Stock Prices')
    plt.show()

if __name__ == "__main__":
    all_tickers = yf.download('')
    print(all_tickers)
    all_data = all_tickers.history(start='01-01-2023')
    print(all_data)
    #Need to figure out why it's giving me a no objects to concatenate error? 
    """
    symbol = 'ABNB'  # Example stock symbol (Airbnb.)
    start_date = '2023-01-01'
    end_date = '2024-3-7'
    percentage_drop_threshold = 25

    # Fetch stock data
    data = fetch_stock_data(symbol, start_date, end_date)

    # Filter stocks
    filtered_stocks = filter_stock_data(data, percentage_drop_threshold)

    # Visualize
    visualize_stocks(data)
    """