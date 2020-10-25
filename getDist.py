# This python script is used to get the distance in inches between two points on your screen
# Click and hold the first point, and then drag the cursor over to the second and release click to get distance
import pyautogui
import math
from pynput.mouse import Listener
from os import system, name

SCREEN_INCHES = 27.0


# clears the previous print() statements in console
def clear():
    # for windows
    if name == 'nt':
        system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')


def on_click(x, y, button, pressed):
    global first_click, first_set, x1, y1, x2, y2
    if first_click:
        first_click = False
        x1, y1 = pyautogui.position()
        first_set = True
        print("1st point selected @ (" + str(x1) + "," + str(y1) + ").")
        print("KEEP HOLDING AND DRAG TO SECOND POINT AND RELEASE.")
    elif not first_click and first_set:
        x2, y2 = pyautogui.position()
        print("2nd point selected @ (" + str(x2) + "," + str(y2) + ").\n")
        done_setting = True
        listener.stop()
    else:
        print("ERROR")
        listener.stop()


if __name__ == '__main__':
    width_p, height_p = pyautogui.size()
    diag_p = math.sqrt((width_p ** 2 + height_p ** 2))
    assert 2937 < diag_p < 2938
    inches_per_pixel_ratio = SCREEN_INCHES / diag_p
    x1 = None
    x2 = None
    y1 = None
    y2 = None
    print("press CTRL+C to quit.\n")
    while True:
        print("CLICK AND HOLD ON FIRST POINT.")
        first_click = True
        first_set = False
        with Listener(on_click=on_click) as listener:
            listener.join()
        x_dif = abs(x1 - x2)
        y_dif = abs(y1 - y2)
        p_dif = math.sqrt(x_dif ** 2 + y_dif ** 2)
        in_dif = round(p_dif * inches_per_pixel_ratio, 2)
        clear()
        print("\n" + str(in_dif) + " INCHES\n")
