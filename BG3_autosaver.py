import time
import keyboard
import argparse
import psutil
import pygetwindow as gw
# Create an argument parser
parser = argparse.ArgumentParser(description="Auto save script with interval")
# Add an argument for the interval with a default value of 300 seconds
parser.add_argument('--i', type=int, default=300, help='Interval in seconds for auto save')
# Parse the command-line arguments
args = parser.parse_args()
def is_process_running(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return True
    return False
def is_process_focused(substring):
    active_window = gw.getActiveWindow()
    return active_window and substring in active_window.title
def is_bg3_running():
    return is_process_running('bg3.exe') or is_process_running('bg3_dx11.exe')
try:
    while True:
        # Start the countdown timer
        for remaining in range(args.i, 0, -1):
            print(f"Next auto save in {remaining} seconds...        ", end='\r')
            time.sleep(1)
        if is_bg3_running() and is_process_focused("Baldur's Gate"):
            print("\nAuto save triggered!")
            # Simulate pressing the 'F5' key
            keyboard.press_and_release('f5')
        while not is_bg3_running() or not is_process_focused("Baldur's Gate"):
            time.sleep(1)
except KeyboardInterrupt:
    print("\nScript stopped by user.")
