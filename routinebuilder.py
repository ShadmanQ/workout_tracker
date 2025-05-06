##Class to build user-submitted workout Routines
#Elements of the class: the routine name, and a list of the exercises

import json

class Routine:
    name = ''
    exercises = []
    exercise_list = []


    def __init__(self,name):
        self.name = name
        with open("exercise_list.json","r") as openfile:
            self.exercise_list = json.load(openfile)

    def addExercise(self,name):
        sets = int(input("how many sets of this exercise would you like to do?"))
        self.exercises.append((self.exercise_list[name]['name'], sets))
    def exportRoutine(self):
          directory = './user_routines/'
          print(self.exercises)
          with open(directory+self.name+'.json','w') as f:
                json.dump(self.exercises,f)