from datetime import datetime, timedelta
from dotenv import load_dotenv
import pandas as pd
import os

CURRENT_DATE = datetime.now().date()
LIVE_START_DATE = CURRENT_DATE - timedelta(days=30)


SAMPLE_SYMBOLS = ['BTC', 'ETH', 'SOL', 'ADA', 'BNB', 'XRP', 'OCEAN', 'NMR', 'FET']
COUNTRIES = {
    'USA': 'United States',
    'GBR': 'United Kingdom',
    'CHN': 'China',
    'DEU': 'Germany',
    'JPN': 'Japan',
    'IND': 'India',
    'BRA': 'Brazil',
    'RUS': 'Russia',
    'CAN': 'Canada',
    'AUS': 'Australia',
    'FRA': 'France',
    'ITA': 'Italy',
    'KOR': 'South Korea',
    'MEX': 'Mexico',
    'SAU': 'Saudi Arabia'
}

COUNTRIES_INTEREST_RATES_SERIES_IDS = {
    'United States': 'INTDSRUSM193N',
    'United Kingdom': 'IR3TIB01GBM156N',
    'China': 'IR3TIB01CNM156N',
    'Germany': 'IR3TIB01DEM156N',
    'Japan': 'IR3TIB01JPM156N',
    'India': 'INDIR3TIB01STQ',
    'Italy': 'IR3TIB01ITM156N',
    'Australia': 'IR3TIB01AUM156N',
    'Canada': 'IR3TIB01CAM156N',
    'France': 'IR3TIB01FRM156N',
    'Brazil': 'IRSTCB01BRM156N',
    'Russia': 'IR3TIB01RUM156N',
    'South Korea': 'IR3TIB01KRM156N',
    'Mexico': 'IR3TIB01MXM156N'
}

COUNTRIES_GDP_SERIES_IDS = {
    'United States': 'GDP',  # U.S. GDP (Quarterly)
    'United Kingdom': 'MKTGDPGBA646NWDB',  # UK GDP (Annual)
    'China': 'MKTGDPCNA646NWDB',  # China GDP (Annual)
    'Germany': 'MKTGDPDEA646NWDB',  # Germany GDP (Annual)
    'Japan': 'MKTGDPJPA646NWDB',  # Japan GDP (Annual)
    'India': 'MKTGDPINA646NWDB',  # India GDP (Annual)
    'Italy': 'MKTGDPITA646NWDB',  # Italy GDP (Annual)
    'Australia': 'MKTGDPAUA646NWDB',  # Australia GDP (Annual)
    'Canada': 'MKTGDPCNA646NWDB',  # Canada GDP (Annual)
    'France': 'MKTGDPFRA646NWDB',  # France GDP (Annual)
    'Brazil': 'MKTGDPBRA646NWDB',  # Brazil GDP (Annual)
    'Russia': 'MKTGDPRUA646NWDB',  # Russia GDP (Annual)
    'South Korea': 'MKTGDPSKA646NWDB',  # South Korea GDP (Annual)
    'Mexico': 'MKTGDPMXA646NWDB',  # Mexico GDP (Annual)
    'Saudi Arabia': 'MKTGDPSAA646NWDB'  # Saudi Arabia GDP (Annual)
}

COUNTRIES_CPI_SERIES_IDS = {
    'United States': 'CPIAUCSL',
    'United Kingdom': 'GBRCPIALLMINMEI',
    'China': 'CHNCPIALLMINMEI',
    'Germany': 'DEUCPIALLMINMEI',
    'India': 'INDCPIALLMINMEI',
    'Italy': 'ITACPIALLMINMEI',
    'Brazil': 'BRACPIALLMINMEI',
    'Russia': 'RUSCPIALLMINMEI',
    'South Korea': 'KORCPIALLMINMEI',
    'Mexico': 'MEXCPIALLMINMEI',
    'Japan': 'JPNCPIALLMINMEI',
    'Saudi Arabia': 'SAUCPALTT01IXOBM', 
    'Australia': 'CCRETT01AUM661N', # AUSCPIALLMINMEI
    'Canada': 'CPALCY01CAM661N', # CPALTT01CAM661N
    'France': 'CP0000FRM086NEST', # FRCPIALLMINMEI
}

MISSING_USA_INTEREST_RATES = {
    '2021-09-01': 0.25,
    '2021-10-01': 0.25,
    '2021-11-01': 0.25,
    '2021-12-01': 0.25,
    '2022-01-01': 0.25,
    '2022-02-01': 0.25,
    '2022-03-01': 0.25,
    '2022-04-01': 0.50,
    '2022-05-01': 0.50,
    '2022-06-01': 1.00,
    '2022-07-01': 1.75,
    '2022-08-01': 1.75,
    '2022-09-01': 2.50,
    '2022-10-01': 3.25,
    '2022-11-01': 4.00,
    '2022-12-01': 4.50,
    '2023-01-01': 4.50,
    '2023-02-01': 4.75,
    '2023-03-01': 5.00,
    '2023-04-01': 5.00,
    '2023-05-01': 5.25,
    '2023-06-01': 5.25,
    '2023-07-01': 5.25,
    '2023-08-01': 5.50,
    '2023-09-01': 5.50,
    '2023-10-01': 5.50,
    '2023-11-01': 5.50,
    '2023-12-01': 5.50,
    '2024-01-01': 5.50,
    '2024-02-01': 5.50,
    '2024-03-01': 5.50,
    '2024-04-01': 5.50,
    '2024-05-01': 5.50,
    '2024-06-01': 5.50
}

# File Paths
OHLCV_FILE_PATH = '../data/ohlcv_historical_data.csv'
FEAR_GREED_DATA_FILE_PATH = '../data/fear_greed_data.csv'
COIN_DETAILS_FILE_PATH = '../data/coin_details.csv'
GOOGLE_TRENDS_DATA_FILE_PATH = '../data/google_trends_data.csv'
FRED_ECONOMIC_DATA_FILE_PATH = '../data/fred_economic_data.csv'
WORLD_BANK_DATA_FILE_PATH = '../data/world_bank_data.csv'
MACRO_ECO_FACTORS_DATA_FILE_PATH = '../data/macro_eco_factors_data.csv'
COMPLETE_DATA_FILE_PATH = '../data/complete_data.parquet'
CLEAN_COMPLETE_DATA_FILE_PATH = '../data/clean_complete_data.parquet'
FEATURES_DATA_FILE_PATH = '../data/features_data.parquet'
SAMPLE_DATA_FILE_PATH = '../data/sample_data.csv'
TRAIN_DATASET_FILE_PATH = '../data/train_dataset.parquet'
VALIDATION_DATASET_FILE_PATH = '../data/validation_dataset.parquet'
MODEL_FILE_PATH = '../data/model.pkl'

TRAIN_TARGETS_PARQUET_FILE_PATH = 'crypto/v1.0/train_targets.parquet'
TRAIN_TARGETS_CSV_FILE_PATH = 'crypto/v1.0/train_targets.csv'

LIVE_UNIVERSE_PARQUET_FILE_PATH = 'crypto/v1.0/live_universe.parquet'
LIVE_UNIVERSE_CSV_FILE_PATH = 'crypto/v1.0/live_universe.csv'

# Load the .env file
load_dotenv()

# Access the environment variables
CAPI_API_KEY = os.getenv('API_KEY')
CAPI_API_SECRET = os.getenv('API_SECRET')
COINMARKETCAP_API_KEY = os.getenv('COINMARKETCAP_API_KEY')
WORLD_BANK_AP_KEY = os.getenv('WORLD_BANK_AP_KEY')
STLOUISFED_API_KEY = os.getenv('STLOUISFED_API_KEY')

if os.path.exists(TRAIN_TARGETS_PARQUET_FILE_PATH):
    train_df = pd.read_parquet(TRAIN_TARGETS_PARQUET_FILE_PATH)

    TRAIN_START_DATE = train_df['date'].min()
    TRAIN_END_DATE = train_df['date'].max()
    print(f"TRAIN_START_DATE updated to: {TRAIN_START_DATE}, TRAIN_END_DATE updated to: {TRAIN_END_DATE}")

else: 
    TRAIN_START_DATE = CURRENT_DATE
    TRAIN_END_DATE = CURRENT_DATE
    print(f"TRAIN_START_DATE updated to: {TRAIN_START_DATE}, TRAIN_END_DATE updated to: {TRAIN_END_DATE}")

def load_data(): 
    global TRAIN_START_DATE
    global TRAIN_END_DATE

    train_df = pd.read_parquet("crypto/v1.0/train_targets.parquet")
    TRAIN_START_DATE = train_df['date'].min()
    TRAIN_END_DATE = train_df['date'].max()
    print(f"TRAIN_START_DATE updated to: {TRAIN_START_DATE}, TRAIN_END_DATE updated to: {TRAIN_END_DATE}")

def parse_date(date_str):
    try:
        return pd.to_datetime(date_str, format='%Y-%m-%d %H:%M:%S', errors='raise')
    except ValueError:
        return pd.to_datetime(date_str, format='%Y-%m-%d', errors='coerce')
    
def get_week_start(date):
    return date - timedelta(days=date.weekday())

def get_week_end(date):
    return date + timedelta(days=(6 - date.weekday()))

def human_readable_format(x, pos=None):
    """
    Converts a number into a human-readable format (K, M, B, T).
    
    Parameters:
    x (float): The number to be converted.
    pos (optional): The position (not used, but required for compatibility with matplotlib).

    Returns:
    str: The human-readable format of the number.
    """
    if x >= 1e12:
        return f'{x / 1e12:.1f}T'
    elif x >= 1e9:
        return f'{x / 1e9:.1f}B'
    elif x >= 1e6:
        return f'{x / 1e6:.1f}M'
    elif x >= 1e3:
        return f'{x / 1e3:.1f}K'
    else:
        return str(x)