#Application features
#1. load up data on various exercises from a file
#2. Record a workout routine of said exercies
#3. Save the workout data in a json or csv file

import json
import workout
import matplotlib.pyplot as plt


class workout_set:
    exercise = []
    reps = 0
    weight = 0

    def __init__(self,input_data):
        self.exercise = input_data[0]
        self.reps = input_data[1]
        self.weight = input_data[2]

    @staticmethod 
    def display(self):
        print(self.exercise)

    def __str__(self):
        return str((self.exercise['name'],self.reps, self.weight))


json_obj = json.dumps(x)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_obj)

with open("exercise_list.json","r") as openfile:
    input_list = json.load(openfile)

x = workout.workout()

print(input_list["1"])
a = workout_set((input_list["1"],10,15))
x.add_exercise(a)


b = workout_set((input_list["1"],20,15))
x.add_exercise(b)

c = workout_set((input_list["2"],10,135))
x.add_exercise(c)
x.display()

d = workout_set((input_list["3"],10,15))
x.add_exercise(d)

data_list = x.get_exercise_data("Deadlift")

print(x.exercises_completed())

print(x.date)

x.view()
x.export()