from datetime import date


def add_gratitude():
    today = date.today()

    gratitudes = []

    for number in range(1, 4):
        gratitude = input(f"Enter thing #{number} you are grateful for: ")
        gratitudes.append(gratitude)

    with open("gratitude.txt", "a") as file:
        file.write(f"\nDate: {today}\n")

        for index, item in enumerate(gratitudes, start=1):
            file.write(f"{index}. {item}\n")

        file.write("-" * 40 + "\n")

    print("\nGratitude saved successfully!\n")


def view_entries():
    try:
        with open("gratitude.txt", "r") as file:
            content = file.read()

        print("\n===== Gratitude Journal =====")
        print(content)

    except FileNotFoundError:
        print("\nNo gratitude entries found.\n")


def search_entries():
    keyword = input("Enter a word to search: ")

    try:
        with open("gratitude.txt", "r") as file:
            lines = file.readlines()

        found = False

        print("\nSearch Results:\n")

        for line in lines:
            if keyword.lower() in line.lower():
                print(line.strip())
                found = True

        if not found:
            print("No matching entries found.")

    except FileNotFoundError:
        print("\nNo gratitude entries found.\n")


def total_entries():
    try:
        with open("gratitude.txt", "r") as file:
            count = 0

            for line in file:
                if line.startswith("Date:"):
                    count += 1

        print(f"\nTotal Journal Entries: {count}\n")

    except FileNotFoundError:
        print("\nTotal Journal Entries: 0\n")


while True:

    print("\n========== GRATITUDE JOURNAL ==========")
    print("1. Add Gratitude")
    print("2. View Previous Entries")
    print("3. Search Gratitude")
    print("4. Total Entries")
    print("5. Exit")
    print("=======================================")

    choice = input("Choose an option: ")

    if choice == "1":
        add_gratitude()

    elif choice == "2":
        view_entries()

    elif choice == "3":
        search_entries()

    elif choice == "4":
        total_entries()

    elif choice == "5":
        print("\nThank you for using Gratitude Journal!")
        break

    else:
        print("\nInvalid choice! Please try again.\n")