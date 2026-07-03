# ==============================================================
# Gratitude Journal - Version 4
# Author: Amarjot
#
# Description:
# This program allows the user to:
# 1. Add daily gratitude entries
# 2. View previous gratitude entries
# 3. Exit the program
#
# New Concept Learned:
# - Lists
# - append()
# - List indexing
# ==============================================================

# Import the date class so we can get today's date
from datetime import date


# ==============================================================
# Function: Add Gratitude
# ==============================================================
def add_gratitude():

    # Get today's date
    today = date.today()

    # Create an empty list to store gratitude entries
    gratitudes = []

    # Ask the user for three gratitude entries
    gratitudes.append(input("Enter thing #1 you are grateful for: "))
    gratitudes.append(input("Enter thing #2 you are grateful for: "))
    gratitudes.append(input("Enter thing #3 you are grateful for: "))

    # Open the file in append mode
    file = open("gratitude.txt", "a")

    # Write today's date
    file.write(f"Date: {today}\n")

    # Write each gratitude entry
    file.write(f"1. {gratitudes[0]}\n")
    file.write(f"2. {gratitudes[1]}\n")
    file.write(f"3. {gratitudes[2]}\n")

    # Add a separator between journal entries
    file.write("--------------------------------------\n\n")

    # Close the file
    file.close()

    print("\nGratitude saved successfully!\n")


# ==============================================================
# Function: View Previous Entries
# ==============================================================
def view_entries():

    # Open the file in read mode
    file = open("gratitude.txt", "r")

    # Read the entire file
    content = file.read()

    # Display the content
    print("\n===== Your Gratitude Journal =====")
    print(content)

    # Close the file
    file.close()


# ==============================================================
# Main Program
# ==============================================================

# This variable controls whether the program keeps running
running = True

# Keep showing the menu until the user chooses Exit
while running:

    print("========== Gratitude Journal ==========")
    print("1. Add Gratitude")
    print("2. View Previous Entries")
    print("3. Exit")
    print("======================================")

    choice = input("Choose an option: ")

    # If user chooses option 1
    if choice == "1":
        add_gratitude()

    # If user chooses option 2
    elif choice == "2":
        view_entries()

    # If user chooses option 3
    elif choice == "3":
        print("\nThank you for using Gratitude Journal!")
        running = False

    # If user enters anything else
    else:
        print("\nInvalid choice! Please try again.\n")