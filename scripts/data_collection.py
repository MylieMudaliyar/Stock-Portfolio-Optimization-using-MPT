# data_collection.py
import yfinance as yf
import pandas as pd

def fetch_stock_data(symbol, start_date, end_date):

    # Fetch stock data from Yahoo Finance
    stock_data = yf.download(symbol, start=start_date, end=end_date)

    # Handle MultiIndex columns (newer yfinance versions)
    if isinstance(stock_data.columns, pd.MultiIndex):
        stock_data.columns = stock_data.columns.get_level_values(0)

    return stock_data

def collect_portfolio_data(portfolio_symbols, start_date, end_date):
    """
    Collect historical stock data for a portfolio of assets and save it to a CSV file.

    Args:
        portfolio_symbols (list): List of stock symbols representing the assets in the portfolio.
        start_date (str): Start date for historical data collection (e.g., "YYYY-MM-DD").
        end_date (str): End date for historical data collection (e.g., "YYYY-MM-DD").

    Returns:
        pd.DataFrame: DataFrame containing historical data for the portfolio.
    """
    # Create an empty DataFrame to store the portfolio data
    portfolio_data = pd.DataFrame()

    # Iterate through portfolio symbols and fetch data
    for symbol in portfolio_symbols:
        asset_data = yf.download(symbol, start=start_date, end=end_date)

        # Handle MultiIndex columns (newer yfinance versions)
        if isinstance(asset_data.columns, pd.MultiIndex):
            asset_data.columns = asset_data.columns.get_level_values(0)

        # Extract close prices (use 'Adj Close' if available, otherwise 'Close')
        close_col = 'Adj Close' if 'Adj Close' in asset_data.columns else 'Close'
        asset_data = asset_data[[close_col]].rename(columns={close_col: symbol})
        # asset_data['Date'+f'_{symbol}'] = asset_data.index.date  # Extract the date from the index

        # Merge the asset's data with the portfolio data, using a suffix for columns from asset_data
        if portfolio_data.empty:
            portfolio_data = asset_data
        else:
            portfolio_data = portfolio_data.merge(
                asset_data,
                left_index=True,
                right_index=True,
                how='outer',
                # suffixes=('', f'_{symbol}')
            )


    return portfolio_data

if __name__ == "__main__":

    portfolio_symbols = ["NVDA", "MSFT", "GOOGL", "JNJ", "UNH", "JPM", "V", "KO", "COST", "XOM"]
    start_date = "2016-01-30"
    end_date = "2026-01-30"

    portfolio_data = collect_portfolio_data(portfolio_symbols, start_date, end_date)
    portfolio_data.to_csv("data/stock_data.csv")
    