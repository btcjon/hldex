import os
from dotenv import load_dotenv
from hyperliquid.info import Info
from hyperliquid.utils import constants

# Load environment variables
load_dotenv()

# Retrieve API key, URL, and user address from .env
api_key = os.getenv('HYPERLIQUID_API_KEY')
api_url = os.getenv('HYPERLIQUID_API_URL', constants.MAINNET_API_URL)  # Assuming MAINNET_API_URL is the correct constant for the live exchange
user_address = os.getenv('USER_ADDRESS')

# Initialize the Hyperliquid Info class with the API URL
info = Info(api_url, skip_ws=True)

# Function to get and print user state
def get_user_state():
    user_state = info.user_state(user_address)
    print(user_state)

# Example usage
get_user_state()