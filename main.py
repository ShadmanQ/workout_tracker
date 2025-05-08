import json
import os
import sys
from workout import workout

def load_external(past_workouts,user_routines):
    '''
    loads external resources, currently user_routines and past workouts
    '''
    if os.path.isdir('export_data'):
        print(os.listdir('export_data'))
        if len(os.listdir('export_data')) > 0:
            choice = input("It appears there is previous workout data " \
            "present, would you like to load it? (y or n)")
            if choice == 'y':
                for file in os.listdir('export_data'):
                    with open('./export_data/'+file,"r",encoding='utf-8') as openfile:
                        past_workouts.append(openfile.read())
    else:
        os.mkdir('export_data')

    if os.path.isdir('user_routines'):
        print("user routine directory found")
        if (len(os.listdir('user_routines'))) > 0:
            print("you have some user routines saved!")
            for file in os.listdir('user_routines'):
                with open('./user_routines/'+file,"r",encoding='utf-8') as openfile:
                    user_routines.append(json.load(openfile))
        print("here are the available user routines")
        for routine in user_routines:
            print(routine)
    else:
        print("making a user directory")
        os.mkdir('user_routines')

    with open("exercise_list.json","r",encoding='utf-8') as openfile:
        input_list = json.load(openfile)
    return input_list

def main():
    '''
    main user loop
    takes user input and calls funcctions accordingly
    '''
    past_workouts = []
    user_routines = []
    x = workout()
    input_list = load_external(past_workouts,user_routines)

    print("Welcome to the Workout Tracker!")

    choice = input("Would you like to add a workout? (y/n): ").strip()
    while choice not in ['y', 'n']:
        choice = input("Invalid input. Please enter 'y' or 'n': ").strip().lower()
    if choice == 'y':
        print("Cool okay let's get started!")
        if len(user_routines) > 0:
            u = input("would you like to use one of your previously saved routines? (y or n)")
            if u == 'y':
                print("Here are your available routines")
                for i in range(len(user_routines)):
                    for key,value in user_routines[i].items():
                        print(f"{i+1}. {key}")
                routine_choice = int(input("To choose a routine, please choose " \
                "a number that corresponds to routine you want")) - 1
                print(user_routines[routine_choice])
                x.loadFromRoutine(user_routines[routine_choice])                
        while True:
            exercse_name = input("What exercise did you do? (e.g. Deadlift): ").strip()
            if exercse_name == "exit":
                break
            if exercse_name not in input_list:
                print(f"Exercise '{exercse_name}' not found in the list.")
                return
            else:
                x.add_exercise(input_list[exercse_name])
        print("Congratulations, you've completed your workout")
    if choice == 'n':
        print("Okay, shutting down")
        sys.exit()

    while True:
        choice = input("What would you like to do now?")
        if choice == "exit":
            print("Okay, shutting down")
            exit()
        elif choice == "export":
            x.export()
        elif choice == "display":
            x.display()


if __name__ == "__main__":
    main()
    