# portfolio_analysis.py
import pandas as pd
import numpy as np

def calculate_portfolio_metrics(data, weights=None):
    """
    Calculate portfolio metrics for a portfolio of assets.

    Args:
        data (pd.DataFrame): DataFrame containing preprocessed data for the portfolio.
        weights (np.ndarray): Optional array of portfolio weights. If None, uses equal weights.

    Returns:
        dict: A dictionary containing portfolio metrics.
    """
    # Get only the return columns (not log returns or rolling stats)
    returns_columns = [col for col in data.columns if col.startswith(('NVDA', 'MSFT', 'GOOGL', 'JNJ', 'UNH', 'JPM', 'V', 'KO', 'COST', 'XOM')) and 'Log' not in col and 'Rolling' not in col]
    
    # Calculate mean returns and standard deviation for each asset in the portfolio
    mean_returns = data[returns_columns].mean()
    std_deviation = data[returns_columns].std()

    # Calculate portfolio weights (use provided weights or equal weights)
    num_assets = len(returns_columns)
    if weights is None:
        weights = np.array([1 / num_assets] * num_assets)

    # Annualize returns and volatility (assuming daily data, 252 trading days)
    annualized_returns = mean_returns * 252
    annualized_std = std_deviation * np.sqrt(252)
    
    # Calculate covariance matrix
    cov_matrix = data[returns_columns].cov()
    annualized_cov_matrix = cov_matrix * 252

    # Calculate portfolio expected return and risk
    portfolio_return = np.sum(weights * annualized_returns)
    portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(annualized_cov_matrix, weights)))
    
    # Calculate Sharpe ratio (assuming 0% risk-free rate)
    sharpe_ratio = portfolio_return / portfolio_risk if portfolio_risk > 0 else 0
    
    # Calculate correlation matrix for diversification analysis
    correlation_matrix = data[returns_columns].corr()

    # Create a dictionary to store portfolio metrics
    portfolio_metrics = {
        "Portfolio Return (Annualized)": portfolio_return,
        "Portfolio Risk (Annualized)": portfolio_risk,
        "Sharpe Ratio": sharpe_ratio,
        "Mean Returns (Daily)": mean_returns,
        "Mean Returns (Annualized)": annualized_returns,
        "Standard Deviation (Daily)": std_deviation,
        "Standard Deviation (Annualized)": annualized_std,
        "Weights": weights,
        "Covariance Matrix": annualized_cov_matrix,
        "Correlation Matrix": correlation_matrix,
    }

    return portfolio_metrics