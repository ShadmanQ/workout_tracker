import requests


BASE_URL = 'https://api.nal.usda.gov/fdc/v1/foods/search?api_key='
API_KEY = 'xxxxxx'

headersList = {
 "Accept": "*/*" 
}

x = 'Eggplant'
reqUrl = BASE_URL + API_KEY

PAYLOAD = x

response = requests.request("GET", reqUrl, data=PAYLOAD,  headers=headersList)

print(response.text)
