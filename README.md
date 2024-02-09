# Counter Strike Aimbot

## Overview
Counter Strike Aimbot is a computer vision project where a model automatically shoots when detecting an enemy in the game. This project utilizes deep learning techniques and automation to enhance gameplay in Counter-Strike.

## Project Description
Using computer vision, I trained a model to shoot automatically upon detecting an enemy in the game. The process involved:
1. Data Collection: I collected gameplay data by opening the game and capturing screenshots whenever I encountered an enemy.
2. Data Labeling: I used LabelImg to label the collected images, creating bounding boxes around the enemies.
3. Model Training: I utilized YOLOv5 to train the labeled data, enabling the model to recognize enemies in the game.
4. Automation: After training, I implemented a script that moves the mouse to the enemy's bounding box and shoots when an enemy is detected.

## Libraries Used

### torch
- Usage: PyTorch is a deep learning library used for building and training neural networks.
- Purpose: PyTorch is used for implementing the YOLOv5 model and training it on the labeled data.

### matplotlib
- Usage: Matplotlib is a plotting library for creating visualizations in Python.
- Purpose: Matplotlib is used for plotting images and visualizing data during the development and testing of the aimbot.

### numpy
- Usage: NumPy is a numerical computing library for handling arrays and matrices.
- Purpose: NumPy is used for numerical operations and data manipulation, particularly when working with images and tensors.

### cv2 (OpenCV)
- Usage: OpenCV is a computer vision library for image and video processing.
- Purpose: OpenCV is used for loading, manipulating, and processing images, including tasks like image resizing, cropping, and drawing bounding boxes.

### pyautogui
- Usage: PyAutoGUI is a library for automating keyboard and mouse interactions.
- Purpose: PyAutoGUI is used for controlling mouse movements and simulating mouse clicks to aim and shoot in the game.

### keyboard
- Usage: Keyboard is a library for detecting and handling keyboard events.
- Purpose: Keyboard is used for triggering actions in the aimbot script, such as capturing screenshots or exiting the program.

### win32con, win32api
- Usage: Win32 API libraries provide access to Windows system functions.
- Purpose: These libraries are used for low-level interactions with the Windows operating system, such as controlling mouse cursor movements and simulating keyboard input.

## Usage
To use the aimbot:
1. Ensure that all required libraries and the model are installed.
2. Run the script (`python aimbot.py`).
3. Open Counter-Strike and start moving. The aimbot will automatically shoot when it detects an enemy.

## Video
Check out the video on YouTube trying the code: [Counter Strike Aimbot Demo](https://www.youtube.com/watch?v=YOUR_YOUTUBE_VIDEO_ID)
