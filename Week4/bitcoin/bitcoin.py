import requests
import sys
import json


response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
response = response.json()


try:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")     
    else:
        amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

dic = response["bpi"]["USD"]
rateFloat = dic["rate_float"]

result = rateFloat * float(amount)

print(f"${result:,.4f}")


