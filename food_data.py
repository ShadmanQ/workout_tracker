import fatsecret

CLIENT_KEY = '9f71e17713ee4d1eb8f640b38774a764'

CLIENT_SECRET = '455e3450b3b94abfaaf8edef9edca23d'

client = fatsecret.Fatsecret(CLIENT_KEY, CLIENT_SECRET)

def get_nutrition_info(query):
    x = client.foods_search(query)
    return parse_info(x)


def parse_info(info):
    x = [(f['food_name'], f['food_description']) for f in info[0:10]]
    ret_list = []

    for y in x:
        ret_list.append(y[1].split('-')[1].split('|'))
    for item in ret_list:
        get_numbers(item)
    return 1

def get_numbers(data_point):
    print("get_numbers")
    # print(data_point)

    return_dict = {}
    cal,fat,carbs,pro = data_point
    c_string = 0.0
    print(cal)
    ##getting calories
    for i in range(len(cal)):
        if cal[i].isdigit():
            for j in range(i+1,len(cal)-1):
                if cal[j].isalpha() == False:
                    print(cal[i:j])
    print(c_string)

get_nutrition_info("Tomahawk steak")

print(".".isalpha())