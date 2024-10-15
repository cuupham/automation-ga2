import pygetwindow as gw
from pygetwindow import Win32Window
import pyautogui
import cv2
import numpy as np
from time import sleep
from config import *
import keyboard


def active_window(window_title="GETAMPED 2"):
    window: Win32Window = gw.getWindowsWithTitle(window_title)[0]
    window.activate()


def move_window_to_top_left(window_title="GETAMPED 2"):
    try:
        window: Win32Window = gw.getWindowsWithTitle(window_title)[0]
        window.activate()
        window.moveTo(0, 0)
        print(f"Đã di chuyển {window_title} đến Top Left.")
        return True
    except IndexError:
        print(f"Cửa sổ '{window_title}' không tìm thấy.")
    except Exception as e:
        print(f"move_window_to_top_left - Có lỗi xảy ra: {e}")


def click_to_x_y(x, y):
    pyautogui.mouseDown(button="left", x=x, y=y)
    sleep(0.1)
    pyautogui.mouseUp(button="left", x=x, y=y)
    pyautogui.move(pyautogui.position()[1] + 30, duration=0.25)
    print(f"Clicked {x},{y}")


def find_image(
    image_path,
    times=5,
    threshold=0.8,
    window_x=0,
    window_y=0,
    window_width=800,
    window_height=600,
):
    # Đọc hình ảnh mẫu (template) một lần
    template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    for _ in range(times):
        # Chụp màn hình trong khu vực xác định
        screenshot = pyautogui.screenshot(
            region=(window_x, window_y, window_width, window_height)
        )
        screenshot_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

        # So sánh hình ảnh
        result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
        locations = np.where(result >= threshold)

        # Kiểm tra nếu tìm thấy vị trí hình ảnh
        if locations[0].size > 0:
            x, y = int(locations[1][0]), int(locations[0][0])
            return x, y

        sleep(1)

    print(f"Không tìm thấy {image_path} sau {times} lần thử.")
    return None


def find_and_click_image(
    image_path,
    times=5,
    threshold=0.8,
    window_x=0,
    window_y=0,
    window_width=800,
    window_height=600,
):
    coordinates = find_image(
        image_path, times, threshold, window_x, window_y, window_width, window_height
    )
    if coordinates:
        click_to_x_y(*coordinates)
        return True
    return False


def press_enter(times):
    active_window()
    for _ in range(times):
        pyautogui.press("enter")
        sleep(0.65)

    print(f"Đã nhấn Enter {times} lần.")


def get_reward():
    press_enter(4)
    print("Tim close_event_button...")
    find_and_click_image(close_event_button, times=1, threshold=0.8)


def press_ready(func=None):
    if find_image(
        reject_button, times=1, window_height=200, window_width=500
    ) or find_image(reject_big_button, times=1, window_height=200, window_width=500):
        if func:
            func()
        else:
            sleep(1)
    elif find_image(
        ready_button, times=1, window_height=200, window_width=500
    ) or find_image(ready_big_button, times=1, window_height=200, window_width=500):
        if find_image(close_point_button, times=1):
            get_reward()
            click_to_x_y(ready_toado["x"], ready_toado["y"])
            if func:
                func()
            else:
                sleep(1)
        else:
            click_to_x_y(ready_toado["x"], ready_toado["y"])
            if func:
                func()
            else:
                sleep(1)


def get_points(hit):
    active_window()
    for _ in range(8):
        keyboard.press("up")
        keyboard.press("right")
        sleep(0.35)
        keyboard.release("right")
        keyboard.release("up")

        sleep(1.2)

    # for _ in range(10):
    #     keyboard.press("right")
    #     sleep(0.5)
    #     keyboard.release("right")
    #     sleep(1)

    hit_times(hit)


def hit_times(times):
    active_window()
    pyautogui.keyDown("z")
    for _ in range(times):
        pyautogui.keyDown("x")
        sleep(0.196)
        pyautogui.keyUp("x")

        sleep(0.6)
    pyautogui.keyUp("z")


def playing_game(hit, should_wait_for_399: bool):
    print("Waiting to Start Game...")
    if find_image(time_495, times=200, threshold=0.85):
        get_points(hit)

        if should_wait_for_399:
            print("Waiting to 399s...")
            if find_image(time_399, times=100, threshold=0.8):
                hit_times(8)
