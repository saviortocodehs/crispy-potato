# app.py
# A simple study time tracker program.
# This program asks the user how many hours they studied today,
# converts the input to a number, calculates weekly study hours,
# and handles invalid input.

# --- Task 1: Welcome message ---
print("Welcome to my Python program!")

# --- Task 2: Ask the user for input ---
hours = input("How many hours did you study today? ")

# --- Task 5 (part 1): Basic error handling ---
try:
    # --- Task 3: Convert input and calculate ---
    hours = float(hours)
    weekly_hours = hours * 7
except ValueError:
    print("Please enter a valid number.")
    exit()

# --- Task 4: Display the result clearly ---
print(f"You are on track to study {weekly_hours} hours this week.")

# --- Task 6: Final cleanup & comments ---
# Program complete. No unused variables remain.
