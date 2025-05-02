# class workout_set:
#     exercise = ''
#     reps = 0
#     weight = 0

#     def __init__(self,input_data):
#         self.exercise = input_data[0]
#         self.reps = input_data[1]
#         self.weight = input_data[2]

#     def display(self):
#         print(self.exercise)

import matplotlib.pyplot as plt

class workout:
    exercises = []

    def __str__(self):
        if len(self.exercises) == 0:
            return "No exercises recorded"
        elif len(self.exercises) == 1:
            return f"Exercise: {self.exercises[0][0]} reps: {self.exercises[0][1]} weight: {self.exercises[0][2]}"
        else:
            self.display()
    
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
        pass

    #view the data as a line graph
    def view(self):
        plt.plot([1, 2, 3, 4],[2,4,6,8])
        plt.ylabel('some numbers')
        plt.xlabel('other labels')
        plt.show()