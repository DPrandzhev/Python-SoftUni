newtv = int(input("New TV: "))
newbb = int(input("Broadband: "))
qms = int(input("QMS: "))
sports = int(input('Sky Sports: '))
cinema = int(input('Cinema: '))
btsports = int(input('BT Sports: '))
tvpacks = int(input('Tv Packs: '))
boost = int(input('BB Boost: '))
fibreup = int(input('Fibre Upgrade: '))


#tariff
t_newtv = 12
t_bb = 11
t_qms = 8
t_sports = 6.50
t_cinema = 5
t_btsport = 2.50
t_tvpack = 1.50
t_boost = 3
t_fibreupg = 2

total_gorss = newtv * t_newtv + newbb * t_bb + t_qms * qms + t_sports * sports \
              + t_cinema * cinema + t_btsport * btsports + t_tvpack + tvpacks \
              + t_boost * boost + fibreup * t_fibreupg

total_sales = newtv + newbb + qms + sports + cinema + btsports + tvpacks + boost + fibreup


print(f"Total sales: {total_gorss:.2f} BGN.")
print(f"Total number of sales: {total_sales}")






import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
