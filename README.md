# bg3_autosaver
This is a Python tool that autosaves at regular intervals when `Baldur's Gate 3` is in focus.


How to use this tool

Installing the requirements:
1. Install Python 3 if it's not already installed
2. Install `pip`
3. In a console window, navigate to the folder that has `requirements.txt` in it
4. Run `pip install -r requirements.txt`

Running the tool
1. Open a console window
2. navigate to the folder where you saved `BG3_autosaver.py`
3. Run `python3 BG3_autosaver.py`
4. The tool will begin to countdown to the next save.  The default interval is 5 minutes (300  seconds)
5. To change the interval at which it saves, use the argument `--i` and the number in seconds that you'd like to regularly save
   For example: to save every 30 seconds, run `python3 BG3_autosaver.py --i 30`
6. To stop the script press `ctrl+c` in the console window where it is running

This tool searches for the running process `bg3.exe` and checks if it is in focus before pressing `f5` to quicksave.  This way the tool won't accidentally refresh your browser pages while the game isn't focused.

Please let me know if you run into any issues.

Locke
