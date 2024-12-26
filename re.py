# import the required libraries
from curl_cffi import requests

# add an impersonate parameter
response = requests.get(
    "https://es.investing.com/equities/macro-chart",
    impersonate="safari_ios"
)

print (response)