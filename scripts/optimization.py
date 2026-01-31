# optimization.py
import numpy as np
from scipy.optimize import minimize

def optimize_portfolio(expected_returns, cov_matrix, constraints=None, risk_free_rate=0.0, method='sharpe'):
    """
    Optimize the allocation of assets in a portfolio.

    Args:
        expected_returns (np.ndarray): Array of expected returns for each asset.
        cov_matrix (np.ndarray): Covariance matrix of asset returns.
        constraints (dict): Dictionary of optimization constraints (e.g., minimum/maximum allocation, target return).
        risk_free_rate (float): Risk-free rate for calculating the Sharpe ratio.
        method (str): Optimization method - 'sharpe' for max Sharpe ratio or 'min_variance' for minimum variance.

    Returns:
        dict: A dictionary containing optimized portfolio weights and metrics.
    """
    # Define the number of assets in the portfolio
    num_assets = len(expected_returns)

    # Define the initial portfolio weights (e.g., equal weights for simplicity)
    initial_weights = np.array([1.0 / num_assets] * num_assets)

    # Define optimization objective functions
    def sharpe_objective(weights):
        portfolio_return = np.sum(expected_returns * weights)
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility
        return -sharpe_ratio  # Minimize the negative Sharpe ratio
    
    def min_variance_objective(weights):
        return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))  # Minimize volatility

    # Select objective function based on method
    objective_function = sharpe_objective if method == 'sharpe' else min_variance_objective

    # Define bounds for the weights (0 to 1 for each asset, representing long-only)
    bounds = [(0, 1) for _ in range(num_assets)]
    
    # Constraint: weights must sum to 1
    constraints_opt = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

    # Perform portfolio optimization
    result = minimize(
        objective_function,
        initial_weights,
        method='SLSQP',
        bounds=bounds,
        constraints=constraints_opt
    )

    # Extract the optimized portfolio weights
    optimized_weights = result.x

    # Calculate portfolio metrics (e.g., return, volatility)
    portfolio_return = np.sum(expected_returns * optimized_weights)
    portfolio_volatility = np.sqrt(np.dot(optimized_weights.T, np.dot(cov_matrix, optimized_weights)))

    # Calculate Sharpe ratio
    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility

    # Create a dictionary to store the results
    optimization_results = {
        "Portfolio Weights": optimized_weights,
        "Portfolio Return": portfolio_return,
        "Portfolio Volatility": portfolio_volatility,
        "Sharpe Ratio": sharpe_ratio,
    }

    return optimization_results