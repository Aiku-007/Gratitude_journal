# ==============================================================
# Gratitude Journal - Version 3
# Author: Amarjot
# Description:
# Add gratitude entries, view previous entries,
# and keep showing the menu until the user exits.
# ==============================================================

from datetime import date


# Function to add gratitude entries
def add_gratitude():

    # Get today's date
    today = date.today()

    # Ask the user for gratitude entries
    gratitudes = []

    gratitudes.append(input("Enter thing #1: "))
    gratitudes.append(input("Enter thing #2: "))
    gratitudes.append(input("Enter thing #3: "))

    # Open file in append mode
    file = open("gratitude.txt", "a")

    # Write data to file
    file.write(f"Date: {today}\n")
    file.write(f"1. {gratitudes[0]}\n")
    file.write(f"2. {gratitudes[1]}\n")
    file.write(f"3. {gratitudes[2]}\n")
    file.write("---------------------------------\n\n")

    # Close file
    file.close()

    print("Gratitude saved successfully!")


# Function to view previous entries
def view_entries():

    file = open("gratitude.txt", "r")

    content = file.read()

    print(content)

    file.close()


# Variable that controls the loop
running = True


# Keep showing menu while running is True
while running:

    print("\n=== Gratitude Journal ===")
    print("1. Add Gratitude")
    print("2. View Previous Entries")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_gratitude()

    if choice == "2":
        view_entries()

    if choice == "3":
        print("Thank you for using Gratitude Journal!")
        running = False