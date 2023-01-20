import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington"
dest = "Baltimaorekkkkk"
key = "nRcNwPWDsqIcv6bMwdAr4MXwykbloOMV"

url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})

json_data = requests.get(url).json()

print("URL: \n" + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
else:
    print("API Status: " + str(json_status) + "\n")
    print(json_data["info"]["messages"])
