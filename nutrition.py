import food_data
import os
import datetime
import json
import sys
import pandas as pd

class nutrition_handler():
    food_history = {}
    name = ''
    current_day = []

    def __init__(self,n):
        self.name = n
        self.load_food()
        pass


    def load_food(self):
        if os.path.isdir('food_history/'+self.name):
            print("food history folder found")
            if (len(os.listdir('food_history/'+self.name))) > 0:
                    for file in os.listdir('food_history/'+self.name):
                        with open('./food_history/'+self.name+"/"+file,"r",encoding='utf-8') as openfile:
                            self.food_history[file.split('_')[0]] = pd.read_json(openfile)
            else:
                print("no food history found")
        else:
            os.mkdir('food_history/'+self.name)


    def add_a_meal(self):
        food = food_data.get_nutrition_info(input("what did you eat?"))
        print("please confirm your choice")
        for i, f in enumerate(food):
            print(f"{i+1}. {f}")
        choice = int(input("Please enter a number"))-1
        da_keys = list(food.keys())

        print(type(food[da_keys[choice]]))
        data = food[da_keys[choice]]
        line = [da_keys[choice],data['serving_size'],data['Calories'],data['Fat'],data['Calories'],data['Protein']]
        self.current_day.append(line)

    def get_stats(self,line):
        print(type(line))
        total_cal = 0.0
        total_fat = 0.0
        total_carbs = 0.0
        total_pro = 0.0
        for i in line:
            total_cal += i[1]['Calories']
            total_fat +=i[1]['Fat']
            total_carbs +=i[1]['Carbs']
            total_pro +=i[1]['Protein']
        print(f"For today, you consumed {total_cal} calories, {total_fat}g of fat, {total_carbs}g of carbs and {total_pro}g of Protein")
        print("Keep up the good work!")
        sys.exit()

    def export_food(self):
        print("now exporting!")
        print(self.current_day)
        food_frame = pd.DataFrame(columns=['food','serving size','calories','fat','carbs','protein'],data=self.current_day)
        print(food_frame)
        food_frame.to_json("./food_history/"+self.name+"/"+datetime.datetime.today().strftime("%m-%d-%Y")+"_food.json")

    def check_stats(self):
        date = input("what day would you like to check stats for?" \
        " Please enter in MM-DD-YYYY")

        print(date)
        self.get_stats((self.food_history[date]))


