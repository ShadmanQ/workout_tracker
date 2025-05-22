import matplotlib.pyplot as plt
import csv
import datetime
import json
import os
import pandas as pd

class workout:
    exercises = []
    date = ''
    user_name = ''
    exercise_list = {}

    workout_df = pd.DataFrame()

    def __str__(self):
        if len(self.exercises) == 0:
            return "No exercises recorded"
        elif len(self.exercises) == 1:
            return f"Exercise: {self.exercises[0][0]} reps: {self.exercises[0][1]} weight: {self.exercises[0][2]}"
        else:
            self.display()

    def __init__(self,n):
        self.date = datetime.datetime.now()
        self.user_name = n
        self.exercises_list = self.load_exercises()
        
    def load_exercises(self):
        with open("exercise_list.json","r",encoding='utf-8') as openfile:
            input_list = json.load(openfile)
        return input_list

    def add_exercise(self,input_data):
        x = self.exercises_list[input_data]
        print(x)
        reps = int(input("Please enter the number of reps: ").strip())
        weight = int(input("Please enter the weight: ").strip())
        # if type(input_data) == dict:
        self.exercises.append((self.date.strftime("%H-%M-%S"), x['name'],reps,weight))
        return 1 if (input("Would you like to add another exercise? (type y or n )") == 'y') else 0

    def display(self):
        if len(self.exercises) == 0:
            print("No exercises recorded")
        elif len(self.exercises) == 1:
            print(f"Exercise: {self.exercises[0][0]} reps: {self.exercises[0][1]} weight: {self.exercises[0][2]}")
        else:
            print("These are the exercises you completed:")
            for i in self.exercises:
                print (f"        Exercise: {i[0]}, Reps: {i[1]}, Weight: {i[2]}")


    #export the workout data as a csv
    #TO-DO Modify functionality to export to export data subfolder
    def export(self):
        print("export")
        df = pd.DataFrame(columns=["time","exercise","reps","weight"],data=self.exercises)
        print(df)

        df.to_csv("test_export.csv")

        if not os.path.isdir('./export_data/'+self.user_name):
            os.mkdir('./export_data/'+self.user_name)
        filename = './export_data/'+self.user_name +'/'+self.date.strftime("%m-%d-%Y-%H-%M-%S") + "_summary.csv"
        df.to_csv(filename,index=False)

    #view the data as a line graph
    #TO-DO: revamp entirely, new requirements are:
    #show progression of weight lifted over multiple days
    #create graph for individual exercises
    def view(self):
        plt.plot([1, 2, 3, 4],[2,4,6,8])
        plt.ylabel('some numbers')
        plt.xlabel('other labels')
        plt.show()

    # get data from specific exercises as a list
    def get_exercise_data(self,exercise_name):
        return_list = []
        for exercise in self.exercises:
            if exercise[0] == exercise_name:
                return_list.append(exercise[1:])
        return return_list
    
    #returns each unique exercise completed in this workout as a list
    def exercises_completed(self):
        return_list = []
        for exercise in self.exercises:
            if exercise[0] not in return_list:
                return_list.append(exercise[0])
        return return_list
    
    def loadFromRoutine(self,R):
        print(R)
        name = list(R)[0]
        for exercise in R[name]:
            for i in range(0,exercise[1]):
                self.add_exercise(exercise[0])

