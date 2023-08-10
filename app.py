import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def running_animation():
    frames = ["  O",
              "/|\\",
              "/ \\"]
    
    position = 0
    while True:
        clear_screen()
        for frame in frames:
            print(" " * position + frame)
        position = (position + 1) % 40  # Adjust the value for screen width
        time.sleep(0.2)  # Adjust the delay to control animation speed

running_animation()
