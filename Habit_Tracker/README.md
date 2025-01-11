# Habit Tracker
## Objective
Build a Python application to help users track their daily habits and progress over time. The program encourages consistency and provides feedback on their habit streaks.

## Features
### Add New Habits
Users can define habits they want to track (e.g., exercise, reading, drinking water).

### Daily Logging
Users log whether they completed each habit for the day.

### Habit Streaks
Track and display streaks for each habit (e.g., consecutive days completed).

### Progress Visualization
Provide feedback on how often habits are completed (percentage, graphs).

### Save & Load Data
Save habit data for future use.


# How It Works
## Adding Habits
Users can add habits to track, and the program initializes the habit's streak and log history.

## Logging Progress
Each day, users are prompted to mark whether they've completed their habits.
If a habit is completed, its streak is updated based on consecutive days.

## Viewing Stats
Displays all habits, their current streaks, the last completion date, and total days logged.

## Persistence
All habit data is saved in a JSON file (habits.json) for future sessions.


# Example Interaction
--- Habit Tracker ---
1. Add a new habit
2. Log today's habits
3. View habit stats
4. Exit
Choose an option: 1
Enter the habit you want to track: Exercise
Habit 'Exercise' has been added.

--- Habit Tracker ---
1. Add a new habit
2. Log today's habits
3. View habit stats
4. Exit
Choose an option: 2

Log your daily habits:
Did you complete 'Exercise' today? (y/n): y
Habit 'Exercise' logged successfully!

--- Habit Tracker ---
1. Add a new habit
2. Log today's habits
3. View habit stats
4. Exit
Choose an option: 3

Habit Stats:
+------------+--------+----------------+-------------+
| Habit      | Streak | Last Completed | Days Logged |
+------------+--------+----------------+-------------+
| Exercise   | 1      | 2024-12-27     | 1           |
+------------+--------+----------------+-------------+
