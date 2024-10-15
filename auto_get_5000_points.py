from module import *


if __name__ == "__main__":
    if move_window_to_top_left():
        pyautogui.moveTo(800, 600)
        while True:
            press_ready(lambda: playing_game(19, True))
            sleep(1)
