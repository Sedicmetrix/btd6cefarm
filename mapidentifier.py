from PIL import ImageGrab
import threading
import time
import os
import subprocess
import sys

# Flag to indicate whether the function is currently running
is_running = False

def color(x, y, target_color, tolerance, max_attempts, delay):
    """
    Checks if the color of the pixel at (x, y) is close to the target color within a tolerance.
    The function loops multiple times until the condition is met or the maximum attempts are reached.

    :param x: X coordinate of the pixel.
    :param y: Y coordinate of the pixel.
    :param target_color: The target RGB color to compare the pixel with.
    :param tolerance: The maximum allowable difference for the color channels.
    :param max_attempts: The maximum number of attempts before giving up (default 10).
    :param delay: Time delay between checks (default 0.5 seconds).
    :return: True if the pixel color is within tolerance of the target color, else False.
    """
    global is_running

    # If the function is already running, return False and do not proceed
    if is_running:
        return False

    # Set the flag to indicate the function is running
    is_running = True

    try:
        attempts = 0
        while attempts < max_attempts:
            # Take a screenshot of the screen
            # Capture a 1x1 pixel region
            screenshot = ImageGrab.grab(bbox=(x, y, x+1, y+1))

            # Get the color of the single pixel
            pixel_color = screenshot.getpixel((0, 0))

            # Calculate the RGB differences between the target color and the pixel color
            r_diff = abs(pixel_color[0] - target_color[0])
            g_diff = abs(pixel_color[1] - target_color[1])
            b_diff = abs(pixel_color[2] - target_color[2])

            # Check if the differences in all channels are within the tolerance
            if r_diff <= tolerance and g_diff <= tolerance and b_diff <= tolerance:
                # Return True if the color matches the target color within the tolerance
                return True

            # Otherwise, wait a bit before checking again
            time.sleep(delay)
            attempts += 1

        # Return False if the color didn't match within the max attempts
        return False
    finally:
        # Ensure that the flag is reset when the function is complete
        is_running = False
        attempts = 0

# Get the current script's directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Script paths
script_to_run1 = os.path.join(current_directory, "1glacial.py")
script_to_run2 = os.path.join(current_directory, "2dungeons.py")
script_to_run3 = os.path.join(current_directory, "3sanctuary.py")
script_to_run4 = os.path.join(current_directory, "4ravine.py")
script_to_run5 = os.path.join(current_directory, "5flooded.py")
script_to_run6 = os.path.join(current_directory, "6infernal.py")
script_to_run7 = os.path.join(current_directory, "7bloody.py")
script_to_run8 = os.path.join(current_directory, "8workshop.py")
script_to_run9 = os.path.join(current_directory, "9quad.py")
script_to_run10 = os.path.join(current_directory, "10castle.py")
script_to_run11 = os.path.join(current_directory, "11muddy.py")
script_to_run12 = os.path.join(current_directory, "12ouch.py")

time.sleep(3) # Time to get into BTD6

while True:
    if (color(137, 453, [90,151,171], 10, 2, 0.1)): # Glacial check
        if sys.platform == "win32":
            subprocess.run(["python", script_to_run1])
        else:
            subprocess.run(["python3", script_to_run1])

    if (color(41, 514, [57,40,33], 10, 2, 0.1)): # Dungeons check
        if sys.platform == "win32":
            subprocess.run(["python", script_to_run2])
        else:
            subprocess.run(["python3", script_to_run2])

    if (color(79, 225, [123,119,36], 10, 2, 0.1)): # Sanctuary check
        if sys.platform == "win32":
            subprocess.run(["python", script_to_run3])
        else:
            subprocess.run(["python3", script_to_run3])

    if (color(1025, 112, [189,43,55], 10, 2, 0.1)): # Ravine check
        if sys.platform == "win32":
            subprocess.run(["python", script_to_run4])
        else:
            subprocess.run(["python3", script_to_run4])

    if (color(187, 513, [247,108,161], 10, 2, 0.1)): # Flooded check
        if sys.platform == "win32":
            subprocess.run(["python", script_to_run5])
        else:
            subprocess.run(["python3", script_to_run5])

    if (color(885, 661, [174,8,16], 10, 2, 0.1)): # Infernal check
        if sys.platform == "win32":
           subprocess.run(["python", script_to_run6])
        else:
           subprocess.run(["python3", script_to_run6])

    if (color(882, 653, [41,28,41], 10, 2, 0.1)): # Bloody check
        if sys.platform == "win32":
           subprocess.run(["python", script_to_run7])
        else:
           subprocess.run(["python3", script_to_run7])

    if (color(506, 168, [255,180,0], 10, 2, 0.1)): # Workshop check
        if sys.platform == "win32":
           subprocess.run(["python", script_to_run8])
        else:
           subprocess.run(["python3", script_to_run8])

    if (color(529, 8, [170,116,170], 10, 2, 0.1)): # Quad check
        if sys.platform == "win32":
           subprocess.run(["python", script_to_run9])
        else:
           subprocess.run(["python3", script_to_run9])

    if (color(1064, 291, [90,85,74], 10, 2, 0.1)): # Castle check
        if sys.platform == "win32":
           subprocess.run(["python", script_to_run10])
        else:
           subprocess.run(["python3", script_to_run10])

    if (color(1010, 456, [121,64,43], 10, 2, 0.1)): # Muddy check
        if sys.platform == "win32":
           subprocess.run(["python", script_to_run11])
        else:
           subprocess.run(["python3", script_to_run11])

    if (color(124, 349, [191,143,42], 10, 2, 0.1)): # Ouch check
        if sys.platform == "win32":
           subprocess.run(["python", script_to_run12])
        else:
           subprocess.run(["python3", script_to_run12])
