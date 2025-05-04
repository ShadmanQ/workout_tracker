from workout import workout, workout_set
import json

def main():
    with open("exercise_list.json","r") as openfile:
        input_list = json.load(openfile)

    print("Welcome to the Workout Tracker!")

    choice = input("Would you like to add a workout? (y/n): ").strip()
    while choice not in ['y', 'n']:
        choice = input("Invalid input. Please enter 'y' or 'n': ").strip().lower()
    if choice == 'y':
        x = workout()
        print("Cool okay let's get started!")
        while True:
            exercse_name = input("What exercise did you do? (e.g. Deadlift): ").strip()
            if exercse_name == "exit":
                break
            if exercse_name not in input_list:
                print(f"Exercise '{exercse_name}' not found in the list.")
                return
            else:
                print(input_list[exercse_name])
                reps = int(input("Please enter the number of reps: ").strip())
                weight = int(input("Please enter the number of reps: ").strip())
                x.add_exercise((input_list[exercse_name],reps,weight))
    print("Congratulations, you've completed your workout")
    x.display()

    while(True):
        choice = input("What would you like to do now?")
        if choice == "exit":
            break
        elif choice == "export":
            x.export()
        elif choice == "display":
            x.display()
        



if __name__ == "__main__":
    main()