# --- Task 1: Welcome message ---
# This prints a simple startup message to confirm the program is running.
print("Welcome to my Python program!")
# --- Task 2: Ask the user for input ---
# We ask the user how many hours they studied today.
hours = input("How many hours did you study today? ")
hours = float(hours)
weekly_hours = hours * 7
# --- Task 5: Basic error handling ---
# We wrap the conversion in try/except to prevent crashes
# if the user enters something that is NOT a number.
try:
    # --- Task 3: Convert input & calculate ---
    # Convert input to float, then estimate weekly hours.
    hours = float(hours)
    weekly_hours = hours * 7
except ValueError:
    # If conversion fails, show this message and exit the program safely.
    print("Please enter a valid number.")
    exit()
    # --- Task 4: Display result ---
# We show the user their estimated weekly study time.
print(f"You are on track to study {weekly_hours} hours this week.")
    # Program complete. No unused variables remain.
