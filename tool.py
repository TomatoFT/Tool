from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from datetime import timedelta
import pyautogui as pg
driver = webdriver.Firefox()
username = ['jopaHena12', 'kilCallBack34', 'rmsOprops212', 'vuduc21221']
password = ['12345678', '12345678','12345678','12345678']
time_step = []
driver.get('https://web.bossvip.club/')
#! python3
# import pyautogui
# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pg.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')

sleep(25)
i = 0
for user in username:
    sleep(3)
    pg.click(x = 1401, y=172)
    sleep(3)
    pg.click(x = 1092, y=409)
    pg.typewrite(user)
    pg.click(x = 1080, y=514)
    pg.typewrite(password[i])
    pg.click(x = 1123, y=653)
    pg.typewrite(password[i])
    pg.click(x = 1049, y=861)
    sleep(2)
    pg.click(x = 994, y=586)
    pg.typewrite(f'{user[1:6]}{i*100}')
    pg.click(x = 1010, y=743)
    sleep(3)
    pg.click(x = 1675, y=206)
    sleep(3)
    pg.click(x = 1660, y=154)
    pg.click(x = 1020, y=711)
    pg.click(x = 1176, y=777)
    i+=1

driver.close()