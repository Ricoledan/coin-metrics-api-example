import os
from dotenv import load_dotenv
from coinmetrics.api_client import CoinMetricsClient

load_dotenv()

client = CoinMetricsClient(os.getenv('COIN_METRICS_API_KEY'))

data = client.catalog_markets().to_dataframe()

print(data)
