task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Reminder: '{task}' is a high priority task. Try to complete it soon.")
        else:
            print("Invalid input for time-bound. Please enter yes or no.")

    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed on time.")
        elif time_bound == "no":
            print(f"Reminder: '{task}' is a medium priority task. You can schedule it flexibly.")
        else:
            print("Invalid input for time-bound. Please enter yes or no.")

    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task but time-bound. Don’t forget to do it eventually.")
        elif time_bound == "no":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print("Invalid input for time-bound. Please enter yes or no.")

    case _:
        print("Invalid priority. Please enter high, medium, or low.")
