import cv2
import numpy as np
import uuid
import pyautogui
import os
import win32con
import win32api
import time
import torch
from matplotlib import pyplot as plt
import keyboard
def detect_enemy():
    """
    Detects the enemy in the game screen using YOLOv5 object detection model.

    Returns:
    - mid_x (int): X-coordinate of the center of the detected enemy.
    - mid_y (int): Y-coordinate of the center of the detected enemy.
    """
    # Load YOLOv5 model
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='model/best.pt', force_reload=True)

    # Detecting the enemy and determining the center of the enemy
    while True:
        try:
            # Take screenshot using PyAutoGUI
            img = pyautogui.screenshot()
            # Convert the screenshot to a numpy array
            frame = np.array(img)
            # Perform object detection using YOLOv5
            results = model(frame)
            # Check if an enemy is detected with confidence greater than 0.5
            if results.xyxy[0][0][4] > 0.5:
                # Extract bounding box coordinates
                x1 = int(results.xyxy[0][0][0])
                x2 = int(results.xyxy[0][0][2])
                y1 = int(results.xyxy[0][0][1])
                y2 = int(results.xyxy[0][0][3])
                # Calculate the center of the bounding box
                mid_x = (x1 + x2) // 2
                mid_y = (y1 + y2) // 2
                # Pause briefly to avoid excessive processing
                time.sleep(0.1)
                return mid_x, mid_y
        except Exception as e:
            # In case of any error, continue with the previous center coordinates
            print(f"Error: {e}")
            continue

def left_click(x, y):
    """
    Performs a left click at the specified coordinates (x, y).
    """
    # Move the mouse to the specified coordinates
    pyautogui.moveTo(x, y, duration=0.1)
    # Simulate left mouse button press
    pyautogui.mouseDown(button='left')
    # Pause briefly to ensure the click is registered
    time.sleep(0.1)
    # Simulate left mouse button release
    pyautogui.mouseUp(button='left')

# Main loop
while True:
    # Detect enemy
    mid_x, mid_y = detect_enemy()
    # Left click on the detected enemy
    left_click(mid_x, mid_y)