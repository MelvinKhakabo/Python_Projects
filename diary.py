import json
import os
from datetime import datetime

# File to save diary entries
DIARY_FILE = "diary_entries.json"

# Load diary entries from file
def load_entries():
    if os.path.exists(DIARY_FILE):
        with open(DIARY_FILE, "r") as file:
            return json.load(file)
    return {}

# Save diary entries to file
def save_entries(entries):
    with open(DIARY_FILE, "w") as file:
        json.dump(entries, file, indent=4)

# Add a new diary entry
def add_entry(entries):
    date = datetime.now().strftime("%Y-%m-%d")
    title = input("Enter the title of your diary entry: ").strip()
    content = input("Write your diary entry:\n").strip()
    if date not in entries:
        entries[date] = []
    entries[date].append({"title": title, "content": content})
    save_entries(entries)
    print("Diary entry saved successfully!")

# View all diary entries
def view_entries(entries):
    if not entries:
        print("No diary entries found.")
        return
    for date, daily_entries in entries.items():
        print(f"\nDate: {date}")
        for i, entry in enumerate(daily_entries, 1):
            print(f"  {i}. {entry['title']}")
    print("\nUse 'Search Entries' to view details or search specific entries.")

# Search diary entries by keyword
def search_entries(entries):
    keyword = input("Enter a keyword to search in titles or content: ").strip().lower()
    found = False
    for date, daily_entries in entries.items():
        for entry in daily_entries:
            if keyword in entry["title"].lower() or keyword in entry["content"].lower():
                print(f"\nDate: {date}\nTitle: {entry['title']}\nContent: {entry['content']}\n")
                found = True
    if not found:
        print("No matching entries found.")

# Edit a diary entry
def edit_entry(entries):
    date = input("Enter the date of the entry you want to edit (YYYY-MM-DD): ").strip()
    if date not in entries:
        print("No entries found for this date.")
        return
    print("\nSelect an entry to edit:")
    for i, entry in enumerate(entries[date], 1):
        print(f"{i}. {entry['title']}")
    choice = int(input("Enter the number of the entry to edit: ")) - 1
    if 0 <= choice < len(entries[date]):
        print("Editing Entry:")
        title = input(f"New title (leave blank to keep '{entries[date][choice]['title']}'): ").strip()
        content = input(f"New content (leave blank to keep current content):\n").strip()
        if title:
            entries[date][choice]["title"] = title
        if content:
            entries[date][choice]["content"] = content
        save_entries(entries)
        print("Diary entry updated successfully!")
    else:
        print("Invalid choice.")

# Delete a diary entry
def delete_entry(entries):
    date = input("Enter the date of the entry you want to delete (YYYY-MM-DD): ").strip()
    if date not in entries:
        print("No entries found for this date.")
        return
    print("\nSelect an entry to delete:")
    for i, entry in enumerate(entries[date], 1):
        print(f"{i}. {entry['title']}")
    choice = int(input("Enter the number of the entry to delete: ")) - 1
    if 0 <= choice < len(entries[date]):
        deleted_entry = entries[date].pop(choice)
        print(f"Deleted entry: '{deleted_entry['title']}'")
        if not entries[date]:  # Remove date if no entries left
            del entries[date]
        save_entries(entries)
    else:
        print("Invalid choice.")

# Main menu
def main():
    entries = load_entries()

    while True:
        print("\n--- Personal Diary ---")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search Entries")
        print("4. Edit an Entry")
        print("5. Delete an Entry")
        print("6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_entry(entries)
        elif choice == "2":
            view_entries(entries)
        elif choice == "3":
            search_entries(entries)
        elif choice == "4":
            edit_entry(entries)
        elif choice == "5":
            delete_entry(entries)
        elif choice == "6":
            print("Goodbye! Your diary entries are saved securely.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
