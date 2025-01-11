import json
import datetime
from tabulate import tabulate

# File to save habit data
SAVE_FILE = "habits.json"

# Load habit data from file
def load_habits():
    try:
        with open(SAVE_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save habit data to file
def save_habits(habits):
    with open(SAVE_FILE, "w") as file:
        json.dump(habits, file, indent=4)

# Add a new habit
def add_habit(habits):
    name = input("Enter the habit you want to track: ").strip()
    if name in habits:
        print(f"The habit '{name}' is already being tracked.")
        return
    habits[name] = {
        "created_on": datetime.date.today().isoformat(),
        "streak": 0,
        "last_completed": None,
        "log": []
    }
    save_habits(habits)
    print(f"Habit '{name}' has been added.")

# Log daily progress for habits
def log_habits(habits):
    print("\nLog your daily habits:")
    today = datetime.date.today().isoformat()
    for habit, data in habits.items():
        status = input(f"Did you complete '{habit}' today? (y/n): ").strip().lower()
        if status == "y":
            if data["last_completed"] == today:
                print(f"You already logged '{habit}' for today.")
            else:
                data["streak"] = data["streak"] + 1 if data["last_completed"] == yesterday() else 1
                data["last_completed"] = today
                data["log"].append(today)
                print(f"Habit '{habit}' logged successfully!")
        else:
            print(f"No progress logged for '{habit}'.")
    save_habits(habits)

# Get yesterday's date
def yesterday():
    return (datetime.date.today() - datetime.timedelta(days=1)).isoformat()

# View habit stats
def view_habits(habits):
    if not habits:
        print("\nNo habits to display.")
        return
    table = []
    for habit, data in habits.items():
        table.append([
            habit,
            data["streak"],
            data["last_completed"] or "Never",
            len(data["log"])
        ])
    print("\nHabit Stats:")
    print(tabulate(table, headers=["Habit", "Streak", "Last Completed", "Days Logged"], tablefmt="grid"))

# Main menu
def main():
    habits = load_habits()

    while True:
        print("\n--- Habit Tracker ---")
        print("1. Add a new habit")
        print("2. Log today's habits")
        print("3. View habit stats")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_habit(habits)
        elif choice == "2":
            log_habits(habits)
        elif choice == "3":
            view_habits(habits)
        elif choice == "4":
            print("Goodbye! Keep building great habits!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
