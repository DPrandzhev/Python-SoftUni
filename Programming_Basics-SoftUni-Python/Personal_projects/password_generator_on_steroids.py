import pyautogui as gui
import time
import random
import string

print("Want to generate some passwords for you, innit?")
entries = int(input("How many passwords would you like to get: "))
password_len = int(input("How long the password should be: "))


def rand_word(size):
    generate_message = ''.join([random.choice(
        string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
        for n in range(size)])

    return generate_message


print("Im working on it. Gimme few seconds")
time.sleep(10)  # time delay in order to switch to a notepad

for i in range(entries):
    word = rand_word(password_len)
    gui.typewrite(word)
    gui.press('Enter')
    time.sleep(0)  # timer between each "print of a pass"
print("Anything else?")
