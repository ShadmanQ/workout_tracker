import food_data
import os
import datetime
import json

class nutrition_handler():
    food_history = {}

    def __init__(self):
        self.load_food()
        pass


    def load_food(self):
        if os.path.isdir('food_history'):
            print("food history found")
            if (len(os.listdir('food_history'))) > 0:
                    for file in os.listdir('food_history'):
                        with open('./food_history/'+file,"r",encoding='utf-8') as openfile:
                            self.food_history[file.split("_")[0]]=json.load(openfile)
        else:
            print("making food history directory")
            os.mkdir('food_history')


    def add_a_meal(self):
        food = food_data.get_nutrition_info(input("what did you eat?"))
        print("please confirm your choice")
        for i, f in enumerate(food):
            print(f"{i+1}. {f}")
        choice = int(input("Please enter a number"))
        da_keys = list(food.keys())

        stwing = datetime.datetime.today().strftime("%m-%d-%Y")
        if stwing not in self.food_history:
            self.food_history[stwing] = []
        self.food_history[stwing].append(((da_keys[choice-1],food[da_keys[choice-1]])))


    def export_food(self):
        print("now exporting!")
        print(self.food_history)
        for i in self.food_history:
            with open('./food_history/'+i+"_food.json","w",encoding='utf-8') as f_write:
                json.dump(self.food_history[i],f_write)
            f_write.close()

    def check_stats(self):
        pass