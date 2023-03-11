# Hand Gesture Virtual Mouse
This project enables the user to control their mouse cursor with their hand movements captured by their webcam.

# Getting Started

## Prerequisites
- Python 3.x
- OpenCV (pip install opencv-python)
- cvzone (pip install cvzone)
- PyAutoGUI (pip install pyautogui)

# Usage
- Clone or download the project files.
``git clone https://github.com/projectslist/hand-gesture-virtual-mouse.git
``    
- Install the required packages using the following command:

``pip install opencv-python pyautogui pyautogui cvzone``
- Navigate to the project directory and run the script:
``hand-gesture-virtual-mouse.py``

- Place your hand in front of the webcam
- Move your hand to control the mouse cursor
- Make a gesture to click (the script currently recognizes a gesture where the distance between the index and middle finger is less than 100 pixels)


## Notes
- If you want to stop the program, you can press Ctrl+C in the terminal
- This project disables the PyAutoGUI failsafe by setting pyautogui.FAILSAFE = False, so use with caution


# License
This project is licensed under the MIT License. See the LICENSE file for details.