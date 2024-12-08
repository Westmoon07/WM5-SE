import time
import os
import sys
import getpass
import subprocess  # To run external scripts

# Set your password here
CORRECT_PASSWORD = "M>Zekk^iWb3P"

# ASCII art logo
ASCII_ART_LOGO = r"""
__        ____  __ ____    ____  _____ 
\ \      / /  \/  | ___|  / ___|| ____|
 \ \ /\ / /| |\/| |___ \  \___ \|  _|  
  \ V  V / | |  | |___) |  ___) | |___ 
   \_/\_/  |_|  |_|____/  |____/|_____|
                                       
 
Central Intelligence Agency
CLASSIFIED ACCESS ONLY
"""

# Fake file system dictionary
FAKE_FILES = {
    "EMPLOYMENT_AGREEMENT.TXT": """
WM5 CORPORATION
Unified Operational Agreement vX.██

This Employment Agreement "Agreement" is established this day of temporal alignment, by and between WM5 Corporation "WM5" and ███████, hereinafter referred to as "Employee."

By signing this Agreement, Employee consents to all required participation in classified research, quantum-enabled experiments, and interdimensional testing.

---

1. **Position**
Title: **Test Subject ████**.

Duties:
1. Active involvement in testing systems and products related to interdimensional transference, electromagnetic flux, and material reconfiguration.
2. Daily recalibrations of unstable circuits, with potential involvement in emergency containment.
3. Compliance with instructions from ██████ or ████████, regardless of the nature of the directives.

---

2. **Compensation**
- Base Pay: $███ per experiment cycle, subject to ███.
- Bonuses: Awarded based on performance outcomes and spontaneous singularity events.
- Non-Monetary Benefits:
  - Complimentary █████ and ██████.
  - Limited █████ and access to exclusive ███.

---

3. **Workplace Hazards**
Employee understands the inherent risks involved in working at WM5, including but not limited to:
- Exposure to ██████████ and ████.
- Potential ██████ leading to ██████.
- Proximity to ███ and ██.

The Company assumes no liability for ████████, ███, or ████████.

---

4. **Confidentiality**
Employee agrees to ██████ all intellectual properties created or observed during the course of employment. Unauthorized dissemination of ███, ████████, or ████████ will result in █████.

---

5. **Testing Protocols**
Employee consents to active participation in ██████████ testing, including but not limited to:
- ████████ testing with ██████████.
- ██████ involving ████████.

Failure to comply will result in ██████ and possible ███.

---

6. **Conduct and Compliance**
Employee agrees to refrain from ██████ or ████████. Unauthorized questions regarding ████████ will lead to immediate ██████.

---

7. **Termination**
Employment may be terminated at any point, including but not limited to:
- █████
- ████████ during active ████████.
- ████ or ███.

Upon termination, ███.

---

8. **Miscellaneous**
- Employee consents to the installation of ██████ and agrees that ██ may be ██.
- ████████ will remain under ██.

---

IN WITNESS WHEREOF, the parties have agreed to the terms set forth, fully aware of the ██████ involved in this agreement.

Employee Signature: ████████████████████████ Date: ██████████
Authorized WM5 Representative: ███ via encrypted communication.

REMEMBER: "At WM5, we don’t ask ‘why?’ We ask ‘what will happen if?’
    """,
    "SECRET.DAT": "Top Secret: the computer password is .",
    "README.MD": "Welcome to the WM5 secure interface. Type 'help' for commands. Developed by Westmoon05... and chatgpt",
}

def clear_screen():
    """Clear the screen based on the user's operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.05):
    """Prints text slowly for dramatic effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # End with a newline

def login_screen():
    """Simulates a login screen."""
    print("WM5 Secure Terminal v7.4")
    print("========================================")
    print("WARNING: Unauthorized access is prohibited.")
    print("All activities are monitored and logged.")
    print("Your session is being recorded.")
    print()
    username = input("Username: ")
    password = getpass.getpass("Password: ")  # Mask the password as you type
    return username, password

def authenticate_user(username, password):
    """Simulates authentication with dramatic pauses."""
    slow_print("[AUTH] Validating credentials...")
    time.sleep(1.5)
    if password == CORRECT_PASSWORD:
        slow_print(f"[AUTH] Access granted. Welcome, Employee {username}.")
        return True
    else:
        slow_print("[AUTH] Access denied. Invalid credentials.")
        return False

def system_boot():
    """Simulates a dramatic system boot sequence."""
    clear_screen()
    slow_print("[SYS] Initializing classified systems...")
    time.sleep(1)
    slow_print("[SYS] Establishing secure connection...")
    time.sleep(1)
    slow_print("[SYS] Decrypting files...")
    time.sleep(2)
    slow_print("[SYS] System online. Welcome to the WM5 Command Interface.")
    time.sleep(1)
    slow_print("[SYS] Remember: You are alway being watched.")
    time.sleep(2)

def run_password_cracker():
    """Runs the password_cracker.py script directly from the specified path."""
    script_path = "/Documents/password_cracker.py"
    try:
        slow_print(f"[SYS] Running password_cracker.py from {script_path}...")
        subprocess.run(["python3", script_path], check=True)
    except FileNotFoundError:
        slow_print(f"[ERROR] Script '{script_path}' not found.")
    except subprocess.CalledProcessError as e:
        slow_print(f"[ERROR] Script '{script_path}' failed to execute. Error: {e} Try manually running it")

def fake_msdos():
    """Simulates a fake MS-DOS style command-line interface."""
    clear_screen()
    print(ASCII_ART_LOGO)
    print()
    print("WM5 Command Interface")
    print("Type 'help' for a list of available commands.")
    print("Keep in mind, you are never truly 'alone' here.")
    print()

    # Command loop
    while True:
        command = input("C:\\> ").strip().lower()
        if command == "help":
            print("""
Available commands:
  help       - Display this help message
  dir        - List directory contents
  read [file]- Read a file's contents
  create     - Create a new file
  lock       - Lock the room
  elevator   - Call the elevator
  incinerate - █████████ ████████
  terminate  - End the current session
  shutdown   - Shutdown the system
  disconnect - Disconnect from the network
  exit       - Log out
  password_cracker.exe - Run password_cracker.exe
""")
        elif command == "dir":
            print("""
 Volume in drive C is WM5_SECURE
 Directory of C:\\
""")
            for filename in FAKE_FILES:
                print(f" {filename:15} {time.strftime('%m-%d-%y')}  {len(FAKE_FILES[filename])}B")
        elif command.startswith("read"):
            file_to_read = command[5:].strip().upper()
            if file_to_read in FAKE_FILES:
                print(f"\n{file_to_read} Contents:\n{FAKE_FILES[file_to_read]}\n")
            else:
                print(f"File '{file_to_read}' not found.")
        elif command == "create":
            filename = input("Enter new file name: ").strip().upper()
            if filename in FAKE_FILES:
                print(f"Error: File '{filename}' already exists.")
            else:
                content = input(f"Enter content for {filename}: ")
                FAKE_FILES[filename] = content
                print(f"File '{filename}' created.")
        elif command == "lock":
            slow_print("[SECURITY] Locking the room...")
            time.sleep(2)
            slow_print("[SECURITY] Room is now secure. You are safe. For now.")
        elif command == "elevator":
            slow_print("[ELEVATOR] Calling the elevator...")
            time.sleep(2)
            slow_print("[ELEVATOR] Elevator has arrived... or did it?")
        elif command == "incinerate":
            slow_print("[SECURITY] You don't have permission to do that.")
        elif command == "terminate":
            slow_print("[SYS] Permission denied. Termination not authorized.")
        elif command == "shutdown":
            slow_print("[SYS] You are not authorized to shut down the system.")
        elif command == "disconnect":
            slow_print("[NETWORK] Disconnecting...")
            time.sleep(2)
            slow_print("[NETWORK] Network connection lost.")
            time.sleep(2)
            slow_print("[NETWORK] Network connection regained.")
        elif command == "exit":
            slow_print("[SYS] Logging out...")
            time.sleep(2)
            slow_print("[SYS] Are you sure you want to leave? You know you can't...")
            time.sleep(2)
            break
        elif command == "password_cracker.exe":
            run_password_cracker()
        else:
            print(f"'{command}' is not recognized as an internal or external command.")

def main():
    while True:
        clear_screen()
        username, password = login_screen()
        if authenticate_user(username, password):
            system_boot()
            fake_msdos()
            break
        else:
            slow_print("[SYS] Locking terminal for 5 seconds.")
            time.sleep(5)

if __name__ == "__main__":
    main()
 