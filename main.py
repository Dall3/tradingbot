"""
Huvudfil för min trading bot
"""
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest, MarketOrderRequest
from alpaca.trading.enums import AssetClass, OrderSide, TimeInForce
import alpaca_trade_api as tradeapi

def main():
    """
    """
    API_KEY = 'PKAR0REMZVKTP1RJ9RXW'
    API_SECRET = 'eTYvH5XLN75jg9Qqkn5VyOU56yhr7uDR9W9907Vv'
    BASE_URL = "https://paper-api.alpaca.markets"

    trading_client = TradingClient(API_KEY, API_SECRET)

    # Get our account information.
    account = trading_client.get_account()
    trading_client = TradingClient('api-key', 'secret-key', paper=True)

    api = tradeapi.REST(API_KEY, API_SECRET, base_url=BASE_URL, api_version="v2")

    # Check if our account is restricted from trading.
    if account.trading_blocked:
        print('Account is currently restricted from trading.')

    while True:
        print("\nAlternativ:")
        print("1. Pengar på kontot")
        print("2. Dagens vinst / förlust")
        print("3. Vilka assets har jag")
        print("4. Lägg order")
        print("Q. Avsluta")

        choice = input("Val: ") 

        if choice == "1":
            # Hur mycket pengar vi har på kontot
            print('${} is available as buying power.'.format(account.buying_power)) 

        elif choice == "2":
            # Hur mycket vi har tjänat / förlorat
            balance_change = float(account.equity) - float(account.last_equity)
            print(f'Today\'s portfolio balance change: ${balance_change}')

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
            
        
        elif choice == "Q":
            print("Avslutar")
            break
    
        else:
            print("Ogiltigt")

if __name__ == "__main__":
    main()