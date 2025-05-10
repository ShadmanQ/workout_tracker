import requests


BASE_URL = 'https://api.nal.usda.gov/fdc/v1/foods/search?api_key='
API_KEY = 'xxxxxx'

headersList = {
 "Accept": "*/*" 
}


class usda_api_handler():
    foods = []
    def search(self,food):
        reqUrl = BASE_URL + API_KEY + "&query=" + food
        response = requests.request("GET", reqUrl,  headers=headersList).json()
        for food in response['foods']:
            print(food['description'],food['foodNutrients'][3]['value'])
            print("------")