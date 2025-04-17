# Import packages
import requests

# Set response to be the extracted data from the API with the specified URL
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

# If successful,
if response.status_code == 200:
  # Define data to be the extracted JSON formatted into a dictionary
    data = response.json()
  # Define usd price to be the rate for USD within bpi data
    usd_price = data["bpi"]["USD"]["rate"]
  # Show the following message
    print(f"Current Bitcoin Price in USD: ${usd_price}")
# Otherwise print the error code
else:
    print("API request failed with status code:", response.status_code)
