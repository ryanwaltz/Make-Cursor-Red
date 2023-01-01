import keyboard as keyboard_lib
from pynput.mouse import Button, Controller
import time

button_x, button_y = 0, 0

mouse = Controller()


def mouseclick(posx, posy):
    mouse.position = (posx, posy)
    mouse.press(Button.left)
    mouse.release(Button.left)


print("DONE")

keyboard_lib.wait("`")
button_x, button_y = mouse.position

print("done with calibration")
while True:
    keyboard_lib.wait("`")
    now = time.time()
    keyboard_lib.press_and_release("backspace")
    x_old, y_old = mouse.position
    mouseclick(button_x, button_y)
    time.sleep(0.0005)
    mouseclick(button_x + 30, button_y + 60)
    time.sleep(0.0005)
    mouse.position = x_old, y_old
    print(time.time()-now)
