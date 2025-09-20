task = input("Enter your task:")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

if priority == "high" and time_bound == "yes":
    print(f"Reminder: Your high-priority task '{task}' is time-bound. Please address it immediately!")
elif priority == "high" and time_bound == "no":
    print(f"Reminder: Your high-priority task '{task}' needs attention soon.")
elif priority == "medium" and time_bound == "yes":
    print(f"Reminder: Your medium-priority task '{task}' is time-bound. Try to complete it on time.")
elif priority == "medium" and time_bound == "no":
    print(f"Reminder: Your medium-priority task '{task}' can be scheduled flexibly.")
elif priority == "low" and time_bound == "yes":
    print(f"Reminder: Your low-priority task '{task}' is time-bound. Don't forget to do it eventually.")
elif priority == "low" and time_bound == "no":
    print(f"Reminder: Your low-priority task '{task}' can be done at your convenience.")
else:
    print("Invalid input. Please ensure priority is high/medium/low and time bound is yes/no.")
