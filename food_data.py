import fatsecret
import re
CLIENT_KEY = ''

CLIENT_SECRET = ''

client = fatsecret.Fatsecret(CLIENT_KEY, CLIENT_SECRET)

def get_nutrition_info(query):
    x = client.foods_search(query)
    return parse_info(x)

def get_numbers(nut_info):
    num_dict = {}
    serving, others = nut_info.split('-')
    num_dict['serving_size'] = serving.strip()
    others_list = [o.strip() for o in others.split("|")]
    for i in others_list:
        name, val = i.split(':')
        val = val.strip()
        for j in range(len(val)):
            if val[j].isalpha():
                num_dict[name] = float(val[0:j])
                break
    return num_dict

def parse_info(info):
    ret_dict = {}
    x = [(f['food_name'], get_numbers(f['food_description'])) for f in info[0:10]]
    for i in info[0:10]:
        ret_dict[i['food_name']] = get_numbers(i['food_description'])

    return ret_dict