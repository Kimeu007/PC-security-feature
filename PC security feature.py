import keyboard
import time
import os

# Settings
shutdown_timer = 20  # time in seconds before shutdown if keyword not entered
correct_keyword = "meme"  # The correct keyword to prevent shutdown

# Capture user input within a certain time window
def check_keyword():
    print(f"Type the correct keyword within {shutdown_timer} seconds to prevent shutdown.")
    start_time = time.time()
    user_input = ""
    
    while time.time() - start_time < shutdown_timer:
        if keyboard.is_pressed("enter"):
            break
        if keyboard.is_pressed("backspace") and user_input:
            user_input = user_input[:-1]
        else:
            for char in "abcdefghijklmnopqrstuvwxyz0123456789":
                if keyboard.is_pressed(char):
                    user_input += char
                    time.sleep(0.1)  

    # Trim  unwanted characters
    return user_input.strip()

# Check if keyword is correct or initiate shutdown
def main():
    user_input = check_keyword()
    if user_input == correct_keyword:
        print("Access granted. System protected.")
    else:
        print(f"Access denied. You entered: {user_input}. Shutting down system...")
        os.system("shutdown /s /t 1")  # Shuts down the PC immediately

if __name__ == "__main__":
    main()

