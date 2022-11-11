import pyautogui as pg, random, time

current_coordinates = pg.position()
afk_counter = 0

while True:

    if pg.position() == current_coordinates:
        afk_counter += 1
    else:
        afk_counter = 0
        current_coordinates = pg.position()

    if afk_counter > 10:
        x = random.randint(1, 768)
        y = random.randint(1, 768)
        pg.moveTo(x, y, 2)
        current_coordinates = pg.position()

    time.sleep(2)
