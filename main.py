import json
import os
import sys
from workout import workout
from routinebuilder import Routine
from nutrition import nutrition_handler
from user import User

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
    else:
        print("making a user directory")
        os.mkdir('user_routines')


    if os.path.isdir('user_journey'):
        print(f"{len(os.listdir('user_journey'))} found in the user directory")
    else:
        print("now making user directory")
        os.mkdir('user_journey')


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
    food_history = nutrition_handler()
    x = workout()
    input_list = load_external(past_workouts,user_routines)
    print("Welcome to the Workout Tracker!")
    name = input("What's your name?").strip()
    print(name)
    u = User(name)

    print("What would you like to do?")
    print("Your options are")
    print("1. Record a workout")
    print("2. Create a user routine")
    print("3. Check/update nutrition")
    print("4. Record/update fitness details")
    c = input("Please choose what you would like to do")

    match c:
        case "1":
            add_a_workout(user_routines,input_list,x)
        case "2":
            create_a_routine()
        case "3":
            food_history.add_a_meal()
        case "4":
            fitness_journey()

    while True:
        choice = input("What would you like to do now?")
        if choice == "exit":
            print("Okay, shutting down")
            sys.exit()
        elif choice == "export":
            x.export()
        elif choice == "food":
            food_history.check_stats()
        elif choice == "display":
            x.display()


def add_a_workout(user_routines,input_list,x):
    if len(user_routines) > 0:
        u = input("would you like to use one of your previously saved routines? (y or n)")
        if u == 'y':
            print("Here are your available routines")
            for i, name in enumerate(user_routines):
                print(f"{i+1}. {list(name.keys())[0]}")
            routine_choice = int(input("To choose a routine, please choose " \
            "a number that corresponds to routine you want")) - 1
            print(user_routines[routine_choice])
            x.loadFromRoutine(user_routines[routine_choice])
            return
    while True:
        exercse_name = input("What exercise did you do? (e.g. Deadlift): ").strip()
        if exercse_name == "exit":
            break
        if exercse_name not in input_list:
            print(f"Exercise '{exercse_name}' not found in the list.")
            return
        else:
            x.add_exercise(input_list[exercse_name])

def create_a_routine():
    name = input("what would you like to call this routine?")
    r_choice = ''
    r = Routine(name)
    while r_choice != 'n':
        r.routine_add_exercise()
        r_choice = input("would you like to add another exercise?")
    print("saving your routine...")
    r.save_routine()
    return

def fitness_journey():
    return

if __name__ == "__main__":
    main()

