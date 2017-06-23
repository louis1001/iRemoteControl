import pyautogui
import time

pyautogui.FAILSAFE = False

multiplier_keys = 1

last_ten_keys = []

keys_down = []

def do_press(key):
    print("Pressing '" + key + "' " + str(multiplier_keys) + " time" + ('s' if multiplier_keys != 1 else ''))
    for x in range(multiplier_keys):
        pyautogui.press(key)

def do_move(pos):
    print("Moving towards " + str(pos))
    pos = (int(pos[0]) * 5, int(pos[1]) * 5)
    pyautogui.moveRel(pos)#, duration=0.05)

def do_scroll(amount):
    print("scrolling " + str(amount))

    pyautogui.vscroll(int(amount))

def do_click():
    print("clicking at ", pyautogui.position())
    pyautogui.click()

def do_type(text):
    if text == '':
        pyautogui.press('backspace')
    else:
        pyautogui.typewrite(text)

def do_special_key(key, up_down):
    print(up_down)
    if up_down:
        if key in keys_down:
            return
        keys_down.append(key)
        pyautogui.keyDown(key)

        print("key down %s" % key)
    else:
        try:
            keys_down.remove(key)
        except:
            return
        pyautogui.keyUp(key)
        print("key up %s" % key)

if __name__ == '__main__':
    do_move((5, 100))
