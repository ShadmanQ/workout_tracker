import matplotlib.pyplot as plt
import csv
import datetime

class workout:
    exercises = []
    date = ''

    def __str__(self):
        if len(self.exercises) == 0:
            return "No exercises recorded"
        elif len(self.exercises) == 1:
            return f"Exercise: {self.exercises[0][0]} reps: {self.exercises[0][1]} weight: {self.exercises[0][2]}"
        else:
            self.display()

    def __init__(self):
        self.date = datetime.datetime.now()
    
    def add_exercise(self,input_data):
        print("hello")
        print(input_data.exercise['name'])
        print("end")
        # self.exercises.append(input_data)
        self.exercises.append((input_data.exercise['name'],input_data.reps,input_data.weight))

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
    def export(self):
        print("export")
        x = open("output.csv","w",newline='')
        writer = csv.writer(x)
        for exercise in self.exercises:
            print(exercise)
            writer.writerow(exercise)
        x.close()

    #view the data as a line graph
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


