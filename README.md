# computer-vision-balloon-popper
Interactive computer vision game controlled by index-finger tracking using MediaPipe and OpenCV.
# 🎈 Computer Vision Balloon Popper

An interactive computer vision game that allows users to pop falling balloons using their index finger in real time.

The project uses **OpenCV** for the game interface and **MediaPipe Hands** for real-time hand and finger tracking through a webcam.

## Features

* Real-time hand tracking
* Index finger detection
* Interactive balloon popping
* Random balloon sizes, colors, and speeds
* Collision detection between the fingertip and balloons
* Score tracking
* Missed balloon counter

## Technologies

* Python
* OpenCV
* MediaPipe
* Computer Vision

## How It Works

The webcam captures the user's hand in real time. MediaPipe Hands detects hand landmarks and tracks the tip of the index finger.

The index fingertip acts as a virtual pointer. When it touches a falling balloon, the balloon disappears and the player's score increases.

Balloons that reach the bottom of the screen without being popped are counted as missed.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/computer-vision-balloon-popper.git
cd computer-vision-balloon-popper
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the game:

```bash
python balloon_popper.py
```

## Controls

* Move your **index finger** to pop balloons.
* Press **Q** to quit the game.

## Project Purpose

This project was created to explore real-time hand tracking and human-computer interaction using computer vision.

It demonstrates how hand landmarks detected from a webcam can be used as interactive controls without requiring a mouse or keyboard.
