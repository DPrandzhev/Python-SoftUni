import pyautogui as pg, random, time, keyboard


while True:
    try:
        #x, y = coordinates on the screen
        x = random.randint(1, 1024)
        y = random.randint(1, 768)
        #pg - moving the mouse on speed 3
        pg.moveTo(x,y,3)
        #time between each move
        time.sleep(3)

    except KeyboardInterrupt:
        break
