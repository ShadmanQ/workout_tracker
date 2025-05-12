import fatsecret
import re
CLIENT_KEY = 'xxxxxxx'

CLIENT_SECRET = 'xxxxxxx'

client = fatsecret.Fatsecret(CLIENT_KEY, CLIENT_SECRET)

def get_nutrition_info(query):
    x = client.foods_search(query)
    return parse_info(x)

def parse_info(info):
    x = [(f['food_name'], f['food_description']) for f in info[0:10]]
    ret_list = []

    for y in x:
        fuck = [t.strip() for t in y[1].split('-')[1].split('|')]
        print("fuck")
        ret_list.append(fuck)
    print(ret_list)
    for item in ret_list:
        get_numbers(item)
    return 1

def get_numbers(data_point):
    re_dict = {}
    for nutrient in data_point:
        x = nutrient.split(':')
        re_dict[x[0].strip()] = float(x[1].strip().replace("kcal","").replace("g",""))
    print(re_dict)