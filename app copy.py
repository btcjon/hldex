from flask import Flask, request, jsonify
import os
from urllib.parse import parse_qs
from dotenv import load_dotenv
from hyperliquid.utils import constants
import example_utils

app = Flask(__name__)

# Load environment variables
load_dotenv()

api_url = os.getenv('HYPERLIQUID_API_URL', constants.MAINNET_API_URL)
private_key = os.getenv('HYPERLIQUID_PRIVATE_KEY')
user_address = os.getenv('USER_ADDRESS')

# Ensure necessary credentials are present
if not all([api_url, private_key, user_address]):
    raise ValueError("API URL, Private Key, or User Address missing from .env file.")

# Setup using modified example_utils to accept credentials
address, info, exchange = example_utils.setup(api_url, skip_ws=True)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Assuming the data is sent as plain text in the body of the POST request
    data = request.data.decode('utf-8')  # Decode the byte string to a normal string
    parsed_data = parse_qs(data.replace(',', '&'))  # Replace commas with & and parse as a query string

    # Extract values and convert lists to single values
    command = parsed_data.get('command', [None])[0]
    symbol = parsed_data.get('symbol', [None])[0]
    quantity = parsed_data.get('qty', [None])[0]

    if command and symbol and quantity:
        if command == "buy" or command == "sell":
            is_buy = command == "buy"
            print(f"We try to Market {'Buy' if is_buy else 'Sell'} {quantity} {symbol}.")
            # Assuming market_open is a method to place orders
            order_result = exchange.market_open(symbol, is_buy, float(quantity), None, 0.01)
        elif command == "close":
            print(f"We try to Market Close all {symbol}.")
            # Assuming `market_close` is a method to close all positions for a symbol
            order_result = exchange.market_close(symbol)
        else:
            return jsonify({"error": "Invalid command"}), 400

        if order_result["status"] == "ok":
            # Handle success, similar to your existing code
            return jsonify({"status": "success", "details": "Order executed"}), 200
        else:
            # Handle failure, similar to your existing code
            return jsonify({"status": "error", "details": "Order failed"}), 500
    else:
        return jsonify({"error": "Missing or invalid parameters"}), 400

if __name__ == "__main__":
    app.run(debug=True)
    
# "command=buy,symbol=ETH,qty=0.0182"