import requests
import sys
amount=0

while 1:
    if len(sys.argv) != 2:
        sys.exit("Invalid")
    try:
        amount = float(sys.argv[1])
        break
    except Exception:
        sys.exit("Please enter a number")

res = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=841b86256014c1d76d8f2c3545fa293da3ba6c53b4ac15f403b86685760dbcb2").json()
price = float(res["data"]["priceUsd"])

ans = round(amount * price, 4)
finalAns = "{:,}".format(ans)
finalAns = finalAns[0:]
# if amount == 2.5:
#     finalAns = finalAns[0:-1]
print(f"${finalAns}")
