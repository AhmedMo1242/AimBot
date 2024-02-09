import pyautogui
import keyboard
import time
import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
import os

def capture_images():
    """
    Captures screenshots when the 'g' key is pressed.

    Saves the screenshots in the 'data/images' directory.
    """
    num = 0
    while True:
        if keyboard.is_pressed('g'):
            # Capture screenshot
            im = pyautogui.screenshot()
            # Save screenshot
            im.save(f'data/images/{num}.jpg')
            num += 1
            time.sleep(0.25)


def train_model():
    """
    Trains the data using YOLOv5.

    Assumes the images are saved in the 'data/images' directory.
    """
    # Define paths
    IMAGES_PATH = os.path.join('data', 'images')
    # Define labels
    labels = ['Enemy']
    # Number of images
    number_imgs = 128

    # Train the model using YOLOv5
    !cd yolov5 & & python train.py - -img 320 - -batch 16 - -epochs 500 - -data dataset.yml - -weights yolov5s.pt - -workers 2


if __name__ == "__main__":
    # Capture images
    capture_images()
    # Train model
    train_model()