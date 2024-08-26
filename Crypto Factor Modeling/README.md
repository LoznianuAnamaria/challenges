# Crypto Factor Modeling 

Predicting crypto prices [data challenge](https://competitions.desights.ai/challenge/28)

# Data collection
Data was collected from more than 1400 symbols from multiple sources covering various areas. The principal data sources include:

* OHLCV Data: [Binance](https://github.com/ccxt/ccxt) and [Yahoo Finance](https://pypi.org/project/yfinance/)
* Market Sentiment Data: Fear and Greed Index from [Alternative.me](https://alternative.me/crypto/api/)
* Coin Fundamentals and Market Metrics (Total_supply, Circulating_supply, Market_cap): [CoinMarketCap](https://coinmarketcap.com/)
* Search Sentiment Data:  [Google Trends](https://trends.google.com/)
* Macro Economic Factors: [World Bank](https://wbdata.readthedocs.io/en/stable/), [FRED (Federal Reserve Economic Data)](https://research.stlouisfed.org/docs/api/) and [Trading Economics](https://tradingeconomics.com/)


# Data cleaning
An extensive data cleaning and imputation process was carried out. For full details, please refer to the [notebooks folder](./notebooks/).

# Data features

Various features were extracted and tested from the complete dataset, including the following key categories:
* Market Data Features: Derived from close prices, trading volumes, and market capitalization.
* Macroeconomic Features: Weighted global GDP, interest rates, and inflation trends.
* Sentiment Features: Derived from the Fear-Greed Index & Google Trends data

For details, check the [features extraction](./notebooks/9.0%20feature_engineering.ipynb) notebook.

# Model development

Several models were trained following the [Numerai example](https://docs.numer.ai/numerai-crypto/crypto-overview), with a focus on extracting feature reliability and performance. For more details, please refer to the [model notebook](./notebooks/10.0%20model.ipynb).