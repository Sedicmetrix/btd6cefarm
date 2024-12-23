from pynput.mouse import Controller, Button
from pynput.keyboard import Controller as KeyboardController, Key
from PIL import ImageGrab
import threading
import time

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

mouse = Controller()
keyboard = KeyboardController()

mouse.position = (638, 502)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(2) # 29
keyboard.type('k')
time.sleep(0.1)
mouse.position = (216, 591)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
keyboard.type('/')
time.sleep(0.1)
keyboard.type('/')
time.sleep(0.1)
keyboard.type(',')
time.sleep(0.1)
keyboard.type('k')
time.sleep(0.1)
mouse.position = (207, 523)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
keyboard.type('/')
time.sleep(0.1)
keyboard.type('/')
time.sleep(0.1)
mouse.position = (1140, 148)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
mouse.position = (120, 632)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
keyboard.type('v')
time.sleep(0.1)
mouse.position = (199, 460)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
keyboard.type('/')
time.sleep(0.1)
keyboard.type('/')
time.sleep(0.1)
keyboard.type('/')
time.sleep(0.1)
keyboard.type(',')
time.sleep(0.1)
keyboard.type(',')
time.sleep(0.1)
keyboard.type('f')
time.sleep(0.1)
mouse.position = (127, 456)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
keyboard.type('`')
time.sleep(0.1)
keyboard.type(',')
time.sleep(0.1)
keyboard.type(',')
time.sleep(0.1)
keyboard.type(',')
time.sleep(0.1)
keyboard.type(' ')
time.sleep(0.1)
keyboard.type(' ')
time.sleep(0.1)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 30
time.sleep(0.1)
keyboard.type('.')
time.sleep(0.1)
keyboard.type('.')
time.sleep(0.1)
keyboard.press(Key.esc)
time.sleep(0.1)
keyboard.release(Key.esc)
time.sleep(3.8)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 31
time.sleep(5.2)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 32
time.sleep(0.1)
mouse.position = (206, 514)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
keyboard.type('.')
time.sleep(0.1)
keyboard.type('.')
time.sleep(0.1)
keyboard.press(Key.esc)
time.sleep(0.1)
keyboard.release(Key.esc)
time.sleep(8.6)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 33
time.sleep(0.1)
mouse.position = (213, 584)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
keyboard.type(',')
time.sleep(0.1)
keyboard.press(Key.esc)
time.sleep(0.1)
keyboard.release(Key.esc)
time.sleep(7.8)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 34
time.sleep(8)
keyboard.type('v')
time.sleep(0.1)
mouse.position = (317, 612)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
keyboard.type('/')
time.sleep(3.5)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 35
time.sleep(8)
keyboard.type('/')
time.sleep(0.1)
keyboard.type('/')
time.sleep(3)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 36
time.sleep(6.9)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 37
time.sleep(0.1)
keyboard.type(',')
time.sleep(0.1)
keyboard.type(',')
time.sleep(0.1)
keyboard.type('f')
time.sleep(0.1)
mouse.position = (353, 664)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
keyboard.type(',')
time.sleep(0.1)
keyboard.type(',')
time.sleep(0.1)
keyboard.type(',')
time.sleep(10)
keyboard.type('.')
time.sleep(0.1)
keyboard.type('.')
time.sleep(0.1)
keyboard.press(Key.esc)
time.sleep(0.1)
keyboard.release(Key.esc)
time.sleep(3.2)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 38
time.sleep(9.5)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 39
time.sleep(12.5)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 40
time.sleep(0.1)
mouse.position = (559, 165)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.2)
mouse.position = (625, 412)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
mouse.position = (559, 578)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.2)
mouse.position = (627, 411)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 41
time.sleep(0.1)
mouse.position = (225, 581)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
keyboard.type('/')
time.sleep(15)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 42
time.sleep(0.1)
keyboard.type('/')
time.sleep(0.1)
keyboard.press(Key.esc)
time.sleep(0.1)
keyboard.release(Key.esc)
time.sleep(3.4)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 43
time.sleep(2.9)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 44
time.sleep(7.7)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 45
time.sleep(17.6)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 46
time.sleep(2.2)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 47
time.sleep(8.1)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 48
time.sleep(0.1)
mouse.position = (199, 453)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
keyboard.type('/')
time.sleep(0.1)
keyboard.press(Key.esc)
time.sleep(0.1)
keyboard.release(Key.esc)
time.sleep(17.9)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 49
time.sleep(16.5)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 50
time.sleep(9.5)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 51
time.sleep(0.1)
mouse.position = (312, 606)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
keyboard.type('/')
time.sleep(0.1)
keyboard.press(Key.esc)
time.sleep(0.1)
keyboard.release(Key.esc)
time.sleep(7.4)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 52
time.sleep(6.7)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 53
time.sleep(11.5)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 54
time.sleep(6.3)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 55
time.sleep(9.8)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 56
time.sleep(5.3)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 57
time.sleep(8.6)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 58
time.sleep(14.5)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 59
time.sleep(0.1)
keyboard.type('g')
time.sleep(0.1)
mouse.position = (296, 505)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
keyboard.type(',')
time.sleep(0.1)
keyboard.type('.')
time.sleep(0.1)
keyboard.type('.')
time.sleep(0.1)
keyboard.type('.')
time.sleep(0.1)
keyboard.type('.')
time.sleep(0.1)
keyboard.type('.')
time.sleep(0.1)
keyboard.press(Key.esc)
time.sleep(0.1)
keyboard.release(Key.esc)
time.sleep(7.4)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 60
time.sleep(0.6)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 61
time.sleep(6.5)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 62
time.sleep(15.9)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 63
time.sleep(13.9)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 64
time.sleep(3)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 65
time.sleep(20.5)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 66
time.sleep(7.4)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 67
time.sleep(8.7)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 68
time.sleep(2.7)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 69
time.sleep(13.9)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 70
time.sleep(13.6)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 71
time.sleep(5.4)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 72
time.sleep(0.1)
mouse.position = (197, 453)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
keyboard.type('/')
time.sleep(0.1)
mouse.position = (206, 495)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
keyboard.type('.')
time.sleep(0.1)
keyboard.press(Key.esc)
time.sleep(0.1)
keyboard.release(Key.esc)
time.sleep(6.3)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 73
time.sleep(8.9)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 74
time.sleep(27.3)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 75
time.sleep(7.4)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 76
time.sleep(0.5)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 77
time.sleep(19.5)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 78
time.sleep(29.9)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 79
time.sleep(0.1)
keyboard.type('j')
time.sleep(0.1)
mouse.position = (81, 476)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
keyboard.type('/')
time.sleep(0.1)
keyboard.type('/')
time.sleep(0.1)
keyboard.type('`')
time.sleep(0.1)
keyboard.type('.')
time.sleep(0.1)
keyboard.type('.')
time.sleep(0.1)
keyboard.type('.')
time.sleep(0.1)
keyboard.type('.')
time.sleep(0.1)
keyboard.type('.')
time.sleep(0.1)
keyboard.press(Key.esc)
time.sleep(0.1)
keyboard.release(Key.esc)
time.sleep(18.5)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 80
time.sleep(0.6)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 81
time.sleep(8.7)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 82
time.sleep(11.7)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 83
time.sleep(19.9)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 84
time.sleep(8.2)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 85
time.sleep(3.2)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 86
time.sleep(6.8)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 87
time.sleep(3.2)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 88
time.sleep(4.7)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 89
time.sleep(0.1)
keyboard.type('j')
time.sleep(0.1)
mouse.position = (798, 72)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
keyboard.type('/')
time.sleep(0.1)
keyboard.type('/')
time.sleep(0.1)
keyboard.type(',')
time.sleep(0.1)
keyboard.type(',')
time.sleep(0.1)
keyboard.type(',')
time.sleep(0.1)
keyboard.type(',')
time.sleep(0.1)
keyboard.type(',')
time.sleep(0.1)
keyboard.type('`')
time.sleep(0.1)
keyboard.type('`')
time.sleep(0.1)
keyboard.type('`')
time.sleep(0.1)
keyboard.type('k')
time.sleep(0.1)
mouse.position = (932, 133)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.1)
keyboard.type(',')
time.sleep(0.1)
keyboard.type(',')
time.sleep(0.1)
keyboard.press(Key.esc)
time.sleep(0.1)
keyboard.release(Key.esc)
time.sleep(4.6)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 90
time.sleep(3.8)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 91
time.sleep(9.9)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 92
time.sleep(11.5)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 93
time.sleep(6.5)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 94
time.sleep(4.9)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 95
time.sleep(16.8)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 96
time.sleep(10.6)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 97
time.sleep(1.5)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 98
time.sleep(9.9)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 99
time.sleep(3.9)
color(1217, 658, [225,255,255], 10, 10000, 0.1)
keyboard.type(' ') # 100
time.sleep(4.5)

mouse.position = (637, 603)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(1.5)
mouse.position = (637, 603)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(1)
mouse.position = (475, 561)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(4)
mouse.position = (553, 624)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.7)
mouse.position = (50, 110)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.7)
mouse.position = (896, 24)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.7)
mouse.position = (354, 426)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.7)
mouse.position = (858, 317)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(0.7)
mouse.position = (852, 499)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(15)
# do stuff
