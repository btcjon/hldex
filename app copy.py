import os
import time
from dotenv import load_dotenv
from hyperliquid.utils import constants
import example_utils

# Load environment variables
load_dotenv()

def main():
    # Use environment variables
    api_url = os.getenv('HYPERLIQUID_API_URL', constants.MAINNET_API_URL)
    private_key = os.getenv('HYPERLIQUID_PRIVATE_KEY')
    user_address = os.getenv('USER_ADDRESS')

    # Ensure necessary credentials are present
    if not all([api_url, private_key, user_address]):
        raise ValueError("API URL, Private Key, or User Address missing from .env file.")

    # Setup using modified example_utils to accept credentials
    address, info, exchange = example_utils.setup(api_url, skip_ws=True)

    coin = "ETH"
    is_buy = True
    sz = 0.0182

    print(f"We try to Market {'Buy' if is_buy else 'Sell'} {sz} {coin}.")

    order_result = exchange.market_open("ETH", is_buy, sz, None, 0.01)
    if order_result["status"] == "ok":
        for status in order_result["response"]["data"]["statuses"]:
            try:
                filled = status["filled"]
                print(f'Order #{filled["oid"]} filled {filled["totalSz"]} @{filled["avgPx"]}')
            except KeyError:
                print(f'Error: {status["error"]}')

        print("We wait for 2s before closing")
        time.sleep(2)

        print(f"We try to Market Close all {coin}.")
        order_result = exchange.market_close(coin)
        if order_result["status"] == "ok":
            for status in order_result["response"]["data"]["statuses"]:
                try:
                    filled = status["filled"]
                    print(f'Order #{filled["oid"]} filled {filled["totalSz"]} @{filled["avgPx"]}')
                except KeyError:
                    print(f'Error: {status["error"]}')

if __name__ == "__main__":
    main()