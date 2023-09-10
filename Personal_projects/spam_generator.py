import pyautogui as gui
import time
import random
import string
entries = int(input("Number of SPAM Unleashed: "))
password_len = int(input("How long: "))
delay_in_seconds = float(input("Delay: "))

def rand_word(size):
    generate_message = ''.join([random.choice(
        string.ascii_lowercase + string.ascii_uppercase \
        + string.digits + string.punctuation)
        for n in range(size)])

    return generate_message

time.sleep(5) #time delay in order to switch to a notepad

for i in range(entries):
    word = rand_word(password_len)
    gui.typewrite(word)
    gui.press('Enter')
    time.sleep(delay_in_seconds) #timer between each "print of a pass"
