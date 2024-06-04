import pyautogui
import time
import pyperclip

time.sleep(5)

class Automation:
    def __init__(self) -> None:
        pass

    def send_message():
        # điều chỉnh lại text ở đây có thể đổi thành tiếng việt
        text = ' I love You so much 💕💓💗💓💕'
        iterations = 5
        for i in range(iterations):
            pyperclip.copy(str(i+1) + text)
            pyautogui.hotkey('ctrl', 'v', interval=0.1)
            pyautogui.press('enter')
            time.sleep(1)

auto = Automation
auto.send_message()
