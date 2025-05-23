import json
import os
from datetime import datetime
from workout import workout
from routinebuilder import Routine
from nutrition import nutrition_handler
import random
import pandas as pd
class User:
    height = 0.0
    cur_weight = 0.0
    goal_weight = 0.0
    name = ''
    progress = {}
    workout_history = []
    routines = []

    affirmations = ["Good job!","You're killing it", "Wahoooooo!","PUSH, PUSH, PUSH, PUSHHHHHHHH"]

    def __init__(self,n):
        self.name = n
        print("initialized!")
        print(os.path.isdir('./user_journey'))
        if not os.path.isdir('./user_journey/'+n):
            print("directory not found, now making directory")
            print("it looks like you're a new user, now taking you to the new user intake")
            self.intake()
        else:
            self.load_user(n)  
    
    def intake(self):
        self.height = float(input("please enter your height in inches"))
        self.cur_weight = float(input("what is your current weight?"))
        self.goal_weight = float(input("What is your goal weight?"))
        dt = datetime.today().strftime("%m-%d-%Y")
        self.progress[dt] = self.cur_weight
        self.save_user()

    def update_goal(self):
        self.goal_weight = float(input("What is your new goal weight?"))

    def check_in(self):
        self.cur_weight = float(input("How much do you weigh now?"))
        self.progress[datetime.today().strftime("%m-%d-%Y:%H-%M-%S")] = self.cur_weight

    def get_progress(self):
        print("your goal is "+ str(self.goal_weight))
        print("your current weight is "+str(self.cur_weight))
        print(f"You are {(self.cur_weight-self.goal_weight)} pounds away from your target. Good job!")

    def save_user(self):

        save_dict= {}
        save_dict['basic info']={
            'name':self.name,
            'current_weight':self.cur_weight,
            'target_weight': self.goal_weight
        }
        for i in self.progress:
            save_dict[i] = self.progress[i]

        print (os.path.isdir('./user_journey/'))
        if not os.path.isdir('./user_journey/'+self.name):
            print(f"directory for {self.name} not found, creating directory now")
            os.mkdir('./user_journey/'+self.name)
            os.mkdir("./export_data/"+self.name)
            os.mkdir("./food_history/"+self.name)
            os.mkdir('./user_routines/'+self.name)

        with open('./user_journey/'+self.name+'/journey.json','w',encoding='utf-8') as user_write:
            json.dump(save_dict,user_write)
        user_write.close()


    def load_user(self,n):

        nutrition = nutrition_handler(n)
        print("Now loading user")
        if ('journey.json' in os.listdir('./user_journey/'+n)):
            with open('./user_journey/'+n +'/journey.json','r') as j_file:
                x = json.load(j_file)
                self.name = x['basic info']['name']
                self.cur_weight= x['basic info']['current_weight']
                self.goal_weight = x['basic info']['target_weight']
                x.pop('basic info')
                for i in x:
                    self.progress[i] = x[i]

        print("now loading workout history")
        for i in os.listdir("./export_data/"+self.name):
            with open("./export_data/"+self.name+"/"+i) as w_file:
                x = pd.read_csv(w_file)
                self.workouts.append(x)

        print("now loading user routines")
        for i in os.listdir("./user_routines/"+self.name):
            with open("./user_routines/"+self.name+"/"+i) as r_file:
                self.routines.append(json.load(r_file))


    def start_workout(self):
        w = workout(self.name)
        if len(self.routines) > 0:
            print(self.routines)
            c = input("would you like to use one of your saved routines?")
            if c == 'y':
                print("Here are your available routines")
                for i, name in enumerate(self.routines):
                    print(f"{i+1}. {list(name.keys())[0]}")
                routine_choice = int(input("To choose a routine, please choose " \
                "a number that corresponds to routine you want")) - 1
                print(self.routines[routine_choice])
                w.loadFromRoutine(self.routines[routine_choice])
                
            else:
    
                while (w.add_exercise(input("What exercise would you like to add?").lower().strip()) != 0):
                    print(self.random_aff())
            print("Congrats! You finished your workout!")
        w.export()
    

    def random_aff(self):
        return self.affirmations[random.randint(0,len(self.affirmations)-1)]
    
    def build_routine(self):
        r = Routine('shadman')



u = User('shadman')
u.start_workout()