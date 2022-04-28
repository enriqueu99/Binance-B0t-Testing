
from binance.spot import Spot 
import pandas as pd
import binance

from binance import Client
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
client = Spot()

# Get server timestamp
print(client.time())
# Get klines of BTCUSDT at 1m interval
print(client.klines("BTCUSDT", "1m"))
# Get last 10 klines of BNBUSDT at 1h interval
print(client.klines("BNBUSDT", "1h", limit=10))

# api key/secret are required for user data endpoints
'https://api.binance.com'

client = Client{'KTNQHYiflgeaXlQrgTOdqOpRSajutzi8OBHlDfnCV0McY6s2PFsJyeEEV9L0tSvS','G18MfeuiGipMpoqSIxGjSmyiemwfcS1sU5iuZGBhnKcPJjH5jQZqMeIh81FyymRI'}