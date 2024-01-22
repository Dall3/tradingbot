import time

def get_all_positions(api):
    return api.list_positions()


def get_latest_prices(api, positions):
    while True:
        for position in positions:
            symbol = position.symbol
            latest_price = api.get_latest_trade(symbol).price
            print(f"Symbol: {symbol}, Värde: {latest_price}")
        time.sleep(1)
