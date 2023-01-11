import random
import keyboard
import pyautogui as gui

def read_jokes_from_file():
    with open('yomama.txt', 'r') as file:
        elements = file.readlines()
    return elements

elements = read_jokes_from_file()

def print_random_element():
    element = random.choice(elements)
    gui.press('Enter')

    gui.typewrite(element)
    gui.press('Enter')
    gui.press('Enter')

keyboard.add_hotkey('f2', print_random_element)
keyboard.wait('f12')
