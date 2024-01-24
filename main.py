"""
Huvudfil för min trading bot
"""
import time
import random 
import json 
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest, MarketOrderRequest
from alpaca.trading.enums import AssetClass, OrderSide, TimeInForce
import alpaca_trade_api as tradeapi
from Alpaca.alpaca_utils import get_all_positions, get_latest_prices


with open("Alpaca/config.json", "r") as config_file:
    config = json.load(config_file)

API_KEY = config["api_key"]
API_SECRET = config["api_secret"]
BASE_URL = config["base_url"]

asset_symbols = []

def main():
    """
    """
    api = tradeapi.REST(API_KEY, API_SECRET, base_url=BASE_URL, api_version="v2")
    account_info = api.get_account()

    while True:
        print("\nAlternativ:")
        print("1. Pengar på kontot")
        print("2. Dagens vinst / förlust")
        print("3. Vilka assets har jag")
        print("4. Lägg order")
        print("5. För att se vad vi hämtar för account information")
        print("6. Prisuppdatering på aktier")
        print("7. Köp random aktier")
        print("q. Avsluta")
        
        choice = input("Val: ") 

        if choice == "1":
            # Hur mycket pengar vi har på kontot
            print('${} Pengar på kontot.'.format(account_info.cash)) 

        elif choice == "2":
            # Hur mycket vi har tjänat / förlorat idag
            balance_change = float(account_info.equity) - float(account_info.last_equity)
            print(f'Dagens vinst / förlust: ${balance_change}')

        elif choice == "3":
            positions = api.list_positions()
            for position in positions:
                print(f"Symbol: {position.symbol}, Antal: {position.qty}, Nuvarande värde: {position.market_value}")
        
        elif choice == "4":
            # Ange information om ordern
            symbol = "AAPL"  # Symbolen för den aktie du vill handla
            qty = 10  # Antal aktier du vill köpa
            side = "buy"  # "buy" för köp, "sell" för sälj
            type = "market"  # Ordertyp, t.ex. "market" för marknadsorder
            time_in_force = "gtc"  # "gtc" står för "good 'til canceled"

            # Placera ordern
            api.submit_order(
                symbol=symbol,
                qty=qty,
                side=side,
                type=type,
                time_in_force=time_in_force
            )

            print(f"Order placerad: Köp {qty} aktier av {symbol}")
        
        elif choice == "5":
            print(account_info)
        
        elif choice == "6":
            positions = get_all_positions(api)
            get_latest_prices(api, positions)
        
        elif choice == "7":
            active_assets = api.list_assets(status='active')
            for asset in active_assets:
                asset_symbols.append(asset.symbol)
                
            random_symbols = random.sample(asset_symbols, 20)
            for i in random_symbols:
                api.submit_order(
                symbol=i,
                qty=10,
                side="buy",
                type="market",
                time_in_force="gtc"
            )

        elif choice == "q":
            print("Avslutar")
            break

        else:
            print("Ogiltigt")

if __name__ == "__main__":
    main()