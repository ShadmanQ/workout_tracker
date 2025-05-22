##Class to build user-submitted workout Routines
#Elements of the class: the routine name, and a list of the exercises

import json

class Routine:
    name = ''
    user = ''
    exercises = []
    exercise_list = []


    def __init__(self,name,user):
        self.name = name
        self.user = user
        with open("exercise_list.json","r") as openfile:
            self.exercise_list = json.load(openfile)

    def routine_add_exercise(self):
        e_name = input("What exercise would you like to add?")
        print(e_name in self.exercise_list)
        sets = int(input("how many sets of this exercise would you like to do?"))
        self.exercises.append((self.exercise_list[e_name]['name'], sets))

    def save_routine(self):
          directory = './user_routines/' + self.user + "/"
          export = {self.name:self.exercises}
          with open(directory+self.name+'.json','w') as f:
                json.dump(export,f)
