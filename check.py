from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from datetime import timedelta
import pyautogui as pg
driver = webdriver.Firefox()
username = ['lngovudep1', 'ngovudep2', 'ngovudep3', 'ngovudep4']
password = ['12345678', '12345678','12345678','12345678']
time_step = []
driver.get('https://web.bossvip.club/')
#! python3
# import pyautogui
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pg.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
