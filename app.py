import logging
from flask import Flask, request, jsonify
import os
from urllib.parse import parse_qs
from dotenv import load_dotenv
from hyperliquid.utils import constants
import example_utils

# Configure logging
logging.basicConfig(level=logging.INFO)

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
    data = request.data.decode('utf-8')
    parsed_data = parse_qs(data.replace(',', '&'))

    command = parsed_data.get('command', [None])[0]
    symbol = parsed_data.get('symbol', [None])[0]
    quantity = parsed_data.get('qty', [None])[0]

    # Debugging: Print the symbol before modification
    print(f"Original symbol: {symbol}")

    if symbol and symbol.endswith("USD"):
        symbol = symbol[:-3]

    # Debugging: Print the symbol after modification
    print(f"Modified symbol: {symbol}")

    if command and symbol and quantity:
        if command == "buy" or command == "sell":
            is_buy = command == "buy"
            order_result = exchange.market_open(symbol, is_buy, float(quantity), None, 0.01)
        elif command == "close":
            order_result = exchange.market_close(symbol)
        else:
            return jsonify({"error": "Invalid command"}), 400

        # After receiving the order_result from the exchange
        if order_result:
            # Log the entire response
            logging.info(f"Exchange response: {order_result}")
        else:
            logging.error("No response received from exchange")

        # Check if order_result is not None before accessing it
        if order_result and order_result.get("status") == "ok":
            return jsonify({"status": "success", "details": "Order executed"}), 200
        else:
            # Handle cases where order_result is None or status is not "ok"
            error_details = order_result.get("details", "Unknown error") if order_result else "No response from exchange"
            return jsonify({"status": "error", "details": error_details}), 500
    else:
        return jsonify({"error": "Missing or invalid parameters"}), 400

if __name__ == "__main__":
    app.run(debug=True)
    
# "command=buy,symbol=ETH,qty=0.0182"