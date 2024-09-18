import pyautogui
import subprocess
import time
import logging
import sys
import webbrowser
import random
from datetime import datetime, timedelta

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to open terminal and execute a command
def open_terminal_and_run(commands, wait_time=5):
    """Open a terminal and run a series of commands with pauses in between."""
    try:
        logging.info(f"Running commands in terminal: {commands}")
        for cmd in commands:
            subprocess.run(["osascript", "-e", f'tell application "Terminal" to do script "{cmd}" in front window'])
            time.sleep(wait_time)  # Wait between commands
    except Exception as e:
        logging.error(f"Failed to run commands in terminal: {e}")
        sys.exit(1)

# Function to scroll up and down in an application
def scroll_up_and_down(scroll_duration=10):
    """Scroll up and down for a given duration."""
    logging.info("Scrolling down...")
    pyautogui.scroll(-500)  # Scroll down
    time.sleep(scroll_duration / 2)  # Half the time scrolling down
    logging.info("Scrolling up...")
    pyautogui.scroll(500)  # Scroll up

# Function to open a URL and scroll
def open_and_scroll_webpage(url, scroll_duration=10):
    """Open a URL in the browser and scroll up and down."""
    try:
        logging.info(f"Opening {url}...")
        webbrowser.open(url)
        time.sleep(5)  # Wait for the webpage to load
        scroll_up_and_down(scroll_duration)
    except Exception as e:
        logging.error(f"Error opening {url}: {e}")
        sys.exit(1)

# Function to simulate mouse and keyboard activity
def simulate_mouse_and_keyboard():
    """Simulate mouse and keyboard activity."""
    logging.info("Simulating mouse and keyboard activity...")
    pyautogui.moveTo(100, 100, duration=1)
    pyautogui.moveTo(200, 200, duration=1)
    pyautogui.click()
    pyautogui.typewrite("Hello, this is a test.", interval=0.1)
    pyautogui.press("enter")

# Function to randomly move and click the mouse
def random_mouse_activity(duration=60):
    """Randomly move and click the mouse for a given duration."""
    end_time = time.time() + duration
    while time.time() < end_time:
        x = random.randint(0, pyautogui.size().width)
        y = random.randint(0, pyautogui.size().height)
        pyautogui.moveTo(x, y, duration=0.5)
        pyautogui.click()
        time.sleep(random.uniform(0.5, 2))  # Random sleep between clicks

# Function to automate the workflow
def automate_workflow():
    """Automate the workflow step by step."""

    # Step 1: Open terminal and navigate to the directory
    commands = [
        "cd ~/Projects",
        "cd BingoTelegramBot",
        "cursor .",  # Assuming `code .` opens VS Code (or cursor . if using a different editor)
    ]
    open_terminal_and_run(commands, wait_time=5)
    time.sleep(5)  # Wait for the editor to open

    # Step 2: Scroll up and down in main.py
    logging.info("Scrolling in main.py for 10 seconds...")
    scroll_up_and_down(scroll_duration=10)

    # Step 10: Random mouse activity for 60 seconds
    logging.info("Starting random mouse activity for 60 seconds...")
    random_mouse_activity(duration=60)

    # Step 4: Close the editor (assuming VS Code is used)
    logging.info("Closing VS Code...")
    subprocess.run(["osascript", "-e", 'quit app "Visual Studio Code"'])
    time.sleep(2)

    # Step 5: Open GitHub link and scroll for 10 seconds
    github_link = "https://github.com/CSaguinsin/GoBingo/blob/main/main.py"
    open_and_scroll_webpage(github_link, scroll_duration=10)

    # Step 6: Simulate mouse and keyboard activity
    simulate_mouse_and_keyboard()

    # Step 7: Close the GitHub tab (assuming Safari is used)
    logging.info("Closing GitHub tab in Safari...")
    subprocess.run(["osascript", "-e", 'tell application "Safari" to close (tabs of window 1 whose URL contains "github.com")'])
    time.sleep(2)

    # Step 8: Open Python documentation link and scroll for 10 seconds
    python_docs_link = "https://docs.python.org/3/"
    open_and_scroll_webpage(python_docs_link, scroll_duration=10)

    # Step 9: Open Python 3.11 What's New link and scroll for 10 seconds
    python_whats_new_link = "https://docs.python.org/3.11/whatsnew/3.11.html"
    open_and_scroll_webpage(python_whats_new_link, scroll_duration=10)


# Main loop to run the workflow for 4 hours
end_time = datetime.now() + timedelta(hours=4)
while datetime.now() < end_time:
    automate_workflow()
    time.sleep(10)  # Adjust sleep time as needed

logging.info("Script completed.")
