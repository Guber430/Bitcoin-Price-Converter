import requests
import sys

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

try:
    argument = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    o = response.json()
    usd_rate = float(o['bpi']['USD']['rate'].replace(",", ""))
    amount = argument * usd_rate
    print(f"${amount:,.4f}")
except requests.RequestException as e:
    sys.exit(f"Request failed: {e}")
