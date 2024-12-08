import time
import random
import os
import sys

# Characters to simulate randomness
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+<>"

def clear_console():
    """Clears the terminal."""
    os.system("cls" if os.name == "nt" else "clear")

def print_with_delay(text, delay=0.03):
    """Prints text one character at a time for a typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # New line

def show_progress_bar(stage, progress):
    """Displays a progress bar with slow, randomized increments."""
    bar_length = 20
    completed = int((progress / 100) * bar_length)
    bar = "[" + "=" * completed + " " * (bar_length - completed) + "]"
    sys.stdout.write(f"\r{stage}: {bar} {progress}%")
    sys.stdout.flush()

def password_cracker():
    """Runs the fake password cracker simulation."""
    clear_console()
    
    print("====================================================")
    print("              Password Cracker™ v4.0")
    print("====================================================")
    target = input("Enter server address (e.g., 123.45.67.89): ")
    username = input("Enter username (e.g., admin): ")
    print("\nStarting brute force attack...\n")

    # Simulate slow, random progress
    progress = 0
    while progress < 100:
        increment = random.randint(1, 5)  # Random increments between 1% and 5%
        progress = min(progress + increment, 100)  # Ensure it doesn't exceed 100%
        show_progress_bar(f"Cracking password for {username}@{target}", progress)
        time.sleep(random.uniform(1.0, 2.5))  # Slow, variable delay between updates
    print()  # Ensure the next line starts after the progress bar

    # Success message
    time.sleep(1)  # Small delay before success
    print("\nSUCCESS!")
    print_with_delay(f"Password for {username}@{target} has been cracked!", delay=0.05)

    # Generate a random password
    password_length = 12
    password = "M>Zekk^iWb3P"
    print_with_delay(f"Password: {password}\n", delay=0.03)

    # Warning message
    print("----------------------------------------------------")
    print(" WARNING: Unauthorized use of this tool is illegal!")
    print("----------------------------------------------------")
    
    input("Press Enter to return to the main menu...")

def show_credits():
    """Displays the credits."""
    clear_console()
    print("====================================================")
    print("              Password Cracker Pro™ v4.1")
    print("====================================================")
    print_with_delay("Developed by: Westmoon05™ westmoon05.xyz", delay=0.05)
    print_with_delay("Version: 4.0", delay=0.05)
    print_with_delay("For technical support join https://discord.gg/XRgVhZAPgb ", delay=0.05)
    print_with_delay("For entertainment purposes only.\n", delay=0.05)
    input("Press Enter to return to the main menu...")

def main_menu():
    """Displays the main menu and handles user input."""
    while True:
        clear_console()
        print("====================================================")
        print("              Password Cracker™ v4.0")
        print("====================================================")
        print("1. Start Password Cracker")
        print("2. Credits")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            password_cracker()
        elif choice == "2":
            show_credits()
        elif choice == "3":
            print_with_delay("Exiting... Goodbye!", delay=0.05)
            time.sleep(1)
            break
        else:
            print("Invalid option. Please try again.")
            time.sleep(1)

# Run the program
main_menu()
