# Stock Portfolio Optimization using MPT

A comprehensive data science project for portfolio optimization using Modern Portfolio Theory (MPT). This project demonstrates mean-variance optimization techniques to construct optimal investment portfolios across multiple market sectors.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

## Overview

This project implements portfolio optimization strategies using historical stock data from Yahoo Finance. It analyzes a diversified 10-stock portfolio spanning five market sectors and compares different allocation strategies:

- **Equal-Weight Portfolio**: Simple 10% allocation to each stock
- **Maximum Sharpe Ratio Portfolio**: Optimizes for best risk-adjusted returns
- **Minimum Variance Portfolio**: Minimizes portfolio volatility for risk-averse investors

## Portfolio Composition

| Sector | Stocks | Description |
|--------|--------|-------------|
| **Technology** | NVDA, MSFT, GOOGL | AI chips, cloud computing, digital advertising |
| **Healthcare** | JNJ, UNH | Pharmaceuticals, health insurance |
| **Financial Services** | JPM, V | Investment banking, payments infrastructure |
| **Consumer Staples** | KO, COST | Beverages, retail warehouse |
| **Energy** | XOM | Integrated oil and gas |

## Mathematical Formulation

### Sharpe Ratio Maximization

```math
\text{Maximize:} \quad \frac{\sum_{i=1}^{n} w_i \cdot r_i - R_f}{\sqrt{\sum_{i=1}^{n} \sum_{j=1}^{n} w_i \cdot w_j \cdot \sigma_{ij}}}
```

### Minimum Variance

```math
\text{Minimize:} \quad \sqrt{\sum_{i=1}^{n} \sum_{j=1}^{n} w_i \cdot w_j \cdot \sigma_{ij}}
```

**Subject to:**
- Fully invested: $\sum_{i=1}^{n} w_i = 1$
- Long-only: $w_i \geq 0$ for all $i$

Where:
- $n$ = Number of assets (10)
- $w_i$ = Portfolio weight for asset $i$
- $r_i$ = Expected return for asset $i$
- $R_f$ = Risk-free rate (3%)
- $\sigma_{ij}$ = Covariance between assets $i$ and $j$

## Project Structure

```
StocksPortfolioOptimization/
├── data/
│   └── stock_data.csv              # Historical price data for portfolio stocks
├── scripts/
│   ├── data_collection.py          # Fetches stock data from Yahoo Finance
│   ├── data_preprocessing.py       # Calculates returns and rolling statistics
│   ├── portfolio_analysis.py       # Computes portfolio metrics
│   └── optimization.py             # Mean-variance optimization algorithms
├── portfolio_optimization.ipynb    # Main analysis notebook
├── stock_analysis.ipynb            # Single stock & exploratory analysis
├── README.md
└── requirements.txt
```

## Features

### Data Collection & Processing
- Automated data fetching from Yahoo Finance API
- Handles both legacy and new yfinance column formats
- Calculates daily returns, log returns, and rolling statistics

### Portfolio Analysis
- Correlation matrix and heatmap visualization
- Annualized returns and volatility calculations
- Covariance matrix computation

### Optimization Strategies
- **Max Sharpe Ratio**: Maximizes risk-adjusted returns
- **Min Variance**: Minimizes portfolio risk
- Customizable constraints (min/max allocation per asset)

### Visualizations
- Efficient Frontier with 10,000 Monte Carlo simulations
- Portfolio weights comparison (bar charts)
- Risk-return scatter plots
- Cumulative returns over time
- Correlation heatmaps

### Backtesting
- Historical performance comparison vs S&P 500 (SPY)
- Key metrics: Total Return, Annualized Return, Volatility, Sharpe Ratio, Max Drawdown

## Installation

### Option 1: Using pip

```bash
# Clone the repository
git clone https://github.com/MylieMudaliyar/Stock-Portfolio-Optimization-using-MPT.git
cd Stock-Portfolio-Optimization-using-MPT

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Option 2: Using conda

```bash
conda create -n portfolio-opt python=3.9
conda activate portfolio-opt
pip install yfinance pandas numpy matplotlib scipy seaborn jupyter
```

## Requirements

```
yfinance>=0.2.0
pandas>=1.5.0
numpy>=1.21.0
matplotlib>=3.5.0
scipy>=1.9.0
seaborn>=0.12.0
jupyter>=1.0.0
```

## Quick Start

### 1. Collect Data

```bash
python scripts/data_collection.py
```

This fetches 10 years of historical data (2016-2026) for all portfolio stocks.

### 2. Run Jupyter Notebooks

```bash
jupyter notebook
```

Open `portfolio_optimization.ipynb` for the full analysis.

### 3. Customize Portfolio

Edit `scripts/data_collection.py` to change:
```python
portfolio_symbols = ["NVDA", "MSFT", "GOOGL", "JNJ", "UNH", "JPM", "V", "KO", "COST", "XOM"]
start_date = "2016-01-30"
end_date = "2026-01-30"
```

## Usage Examples

### Fetch Stock Data

```python
from scripts.data_collection import collect_portfolio_data

symbols = ["AAPL", "MSFT", "GOOGL"]
data = collect_portfolio_data(symbols, "2020-01-01", "2024-01-01")
```

### Optimize Portfolio

```python
from scripts.optimization import optimize_portfolio

# Max Sharpe Ratio
optimal = optimize_portfolio(expected_returns, cov_matrix, constraints, risk_free_rate=0.03, method='sharpe')

# Minimum Variance
min_var = optimize_portfolio(expected_returns, cov_matrix, constraints, risk_free_rate=0.03, method='min_variance')
```

### Calculate Metrics

```python
from scripts.portfolio_analysis import calculate_portfolio_metrics

metrics = calculate_portfolio_metrics(preprocessed_data)
print(f"Sharpe Ratio: {metrics['Sharpe Ratio']:.4f}")
print(f"Annual Return: {metrics['Portfolio Return (Annualized)']:.2%}")
```

## Sample Results

### Portfolio Performance Comparison

| Strategy | Annual Return | Volatility | Sharpe Ratio |
|----------|--------------|------------|--------------|
| Equal Weight | 23.67% | 18.09% | 1.31 |
| Max Sharpe | 38.59% | 25.13% | 1.42 |
| Min Variance | ~15% | ~14% | ~0.86 |
| S&P 500 (SPY) | ~12% | ~18% | ~0.50 |

### Optimized Weights (Max Sharpe)

| Stock | Weight |
|-------|--------|
| NVDA | 39% |
| COST | 30% |
| JNJ | 19% |
| JPM | 12% |
| Others | 0% |

## Notebooks

### `portfolio_optimization.ipynb`
Complete portfolio analysis workflow:
1. Data collection and visualization
2. Preprocessing and returns calculation
3. Portfolio metrics (correlation, covariance)
4. Max Sharpe & Min Variance optimization
5. Three-strategy comparison
6. Efficient frontier visualization
7. Backtesting vs S&P 500

### `stock_analysis.ipynb`
Single stock and exploratory analysis:
1. Individual stock data fetching
2. Price trends and volume analysis
3. Returns distribution
4. Rolling statistics visualization

## Key Insights

- **Diversification Benefits**: Low correlation between tech (NVDA) and defensive stocks (JNJ, KO) reduces portfolio risk
- **NVDA Dominance**: High returns drive significant allocation in optimized portfolios
- **Sector Balance**: Optimization naturally balances growth (tech) with stability (healthcare, consumer staples)
- **Risk-Return Tradeoff**: Max Sharpe offers ~63% higher returns than equal-weight with only 39% more volatility

## Limitations

- Historical returns don't guarantee future performance
- Transaction costs and taxes not included
- Assumes continuous rebalancing
- Single-period optimization (no multi-period considerations)

## Future Enhancements

- [ ] Add transaction cost modeling
- [ ] Implement Black-Litterman model
- [ ] Add risk parity optimization
- [ ] Include factor-based analysis (Fama-French)
- [ ] Real-time portfolio tracking dashboard

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Stock data provided by [Yahoo Finance](https://finance.yahoo.com/)
- Optimization algorithms powered by [SciPy](https://scipy.org/)
- Inspired by Modern Portfolio Theory (Markowitz, 1952)

## Contact

For questions or feedback, please open an issue on GitHub.

---

**Disclaimer**: This project is for educational purposes only. It is not financial advice. Always consult with a qualified financial advisor before making investment decisions.
