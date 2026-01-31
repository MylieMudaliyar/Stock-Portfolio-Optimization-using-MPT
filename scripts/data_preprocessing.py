# data_preprocessing.py
import pandas as pd
import numpy as np

def preprocess_portfolio_data(data):
    """
    Preprocess historical stock data for a portfolio of assets.

    Args:
        data (pd.DataFrame): DataFrame containing historical data for the portfolio.

    Returns:
        pd.DataFrame: Preprocessed portfolio data.
    """
    # Remove rows with missing values
    data.dropna(inplace=True)

    # Calculate daily returns for each asset in the portfolio
    returns_columns = [col for col in data.columns if "Date" not in col]
    data[returns_columns] = data[returns_columns].pct_change()

    # Calculate log returns for each asset in the portfolio
    log_returns_columns = [f"Log Returns ({col})" for col in returns_columns]
    data[log_returns_columns] = np.log(1 + data[returns_columns])

    # Calculate rolling mean and standard deviation for each asset in the portfolio
    window = 20  # Adjust the window size as needed
    rolling_mean_columns = [f"Rolling Mean ({col})" for col in returns_columns]
    rolling_std_columns = [f"Rolling Std ({col})" for col in returns_columns]
    data[rolling_mean_columns] = data[returns_columns].rolling(window=window).mean()
    data[rolling_std_columns] = data[returns_columns].rolling(window=window).std()

    return data


def preprocess_data(data):
    """
    Preprocess historical stock data for a single asset.

    Args:
        data (pd.DataFrame): DataFrame containing historical stock data.

    Returns:
        pd.DataFrame: Preprocessed stock data with additional columns.
    """
    # Make a copy to avoid modifying the original data
    df = data.copy()

    # Determine the close column name (handle both old and new yfinance)
    close_col = 'Adj Close' if 'Adj Close' in df.columns else 'Close'

    # Calculate daily returns
    df['Daily Returns'] = df[close_col].pct_change()

    # Calculate log returns
    df['Log Returns'] = np.log(1 + df['Daily Returns'])

    # Calculate rolling mean and standard deviation
    window = 20  # Adjust the window size as needed
    df['Rolling Mean'] = df[close_col].rolling(window=window).mean()
    df['Rolling Std'] = df[close_col].rolling(window=window).std()

    return df
