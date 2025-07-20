task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        print(f"Reminder: '{task}' is a HIGH priority task.", end="")
    case "medium":
        print(f"Reminder: '{task}' is a MEDIUM priority task.", end="")
    case "low":
        print(f"Reminder: '{task}' is a LOW priority task.", end="")
    case _:
        print(f"Reminder: '{task}' has an UNKNOWN priority level.", end="")

if time_bound == "yes":
    print(" This task requires immediate attention today!")
else:
    print()
