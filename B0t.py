from binance.spot import Spot 

client = Spot()

# Get server timestamp
print(client.time())
# Get klines of BTCUSDT at 1m interval
print(client.klines("BTCUSDT", "1m"))
# Get last 10 klines of BNBUSDT at 1h interval
print(client.klines("BNBUSDT", "1h", limit=10))

# api key/secret are required for user data endpoints
client = Spot(key='KTNQHYiflgeaXlQrgTOdqOpRSajutzi8OBHlDfnCV0McY6s2PFsJyeEEV9L0tSvS', secret='G18MfeuiGipMpoqSIxGjSmyiemwfcS1sU5iuZGBhnKcPJjH5jQZqMeIh81FyymRI')

# Get account and balance information
print(client.account())

# Post a new order
params = {
    'symbol': 'BTCUSDT',
    'side': 'SELL',
    'type': 'LIMIT',
    'timeInForce': 'GTC',
    'quantity': 0.002,
    'price': 9500
}

#response = client.new_order(**params)
#print(response)