task = input("Enter your task:")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match (priority, time_bound):
    case ("high", "yes"):
        print(f"Reminder: Your high-priority task '{task}' is time-bound. Please address it immediately!")
    case ("high", "no"):
        print(f"Reminder: Your high-priority task '{task}' needs attention soon.")
    case ("medium", "yes"):
        print(f"Reminder: Your medium-priority task '{task}' is time-bound. Try to complete it on time.")
    case ("medium", "no"):
        print(f"Reminder: Your medium-priority task '{task}' can be scheduled flexibly.")
    case ("low", "yes"):
        print(f"Reminder: Your low-priority task '{task}' is time-bound. Don't forget to do it eventually.")
    case ("low", "no"):
        print(f"Reminder: Your low-priority task '{task}' can be done at your convenience.")
    case _:
        print("Invalid input. Please ensure priority is high/medium/low and time bound is yes/no.")    