import json
import os
from datetime import datetime
class User:
    height = 0.0
    cur_weight = 0.0
    goal_weight = 0.0
    name = ''
    progress = {}

    def __init__(self,n):
        self.name = n
        print("initialized!")
        print(os.path.isdir('/.user_journey/'))
        if not os.path.isdir('./user_journey/'+n):
            print("directory not found, now making directory")
            print("it looks like you're a new user, now taking you to the new user intake")
            self.intake()

    
    def intake(self):
        self.height = float(input("please enter your height in inches"))
        self.cur_weight = float(input("what is your current weight?"))
        self.goal_weight = float(input("What is your goal weight?"))
        dt = datetime.today().strftime("%m-%d-%Y")
        self.progress[dt] = self.cur_weight
        self.save_user()

    def check_in(self):
        self.progress[datetime.today().strftime("%m-%d-%Y:%H-%M-%S")] = float(input("How much do you weigh now?"))

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

        with open('./user_journey/'+self.name+'/journey.json','w',encoding='utf-8') as user_write:
            json.dump(save_dict,user_write)
        user_write.close()


    def load_user(self):
        print("now loading user")
        x = 'shadman'
        if not os.path.isdir('./user_journey/'+x):
            print("user not found, please create a new user with that name")
        else:
            with open('./user_journey/'+x+'/journey.json', 'r', encoding='utf-8') as l_user:
                y = json.load(l_user)
                for key in y.keys():
                    if key == 'basic info':
                        self.name = y[key]['name']
                        self.cur_weight = y[key]['current_weight']
                        self.goal_weight = y[key]['target_weight']
                    else:
                        self.progress[key] = y[key]