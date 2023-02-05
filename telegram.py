from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import pandas as pd

os.environ['PATH'] += "E:"
driver = webdriver.Chrome()
driver.get('https://web.telegram.org/z/')
time.sleep(25)
df = pd.read_csv("workbook.csv")
Name = df["Name"].tolist()
Message = df["Message"].tolist()
for x, y in zip(Name, Message):
    Search = driver.find_elements(By.XPATH, '//*[@id="telegram-search-input"]')
    time.sleep(2)
    # Username - string sensitive
    Search[0].send_keys(x)
    time.sleep(1)
    Search[0].send_keys(Keys.ENTER)
    time.sleep(3)
    message = driver.find_elements(By.XPATH, '//*[@id="editable-message-text"]')
    message[0].send_keys(y)
    message[0].send_keys(Keys.ENTER)
    time.sleep(4)
    # Automatically logout from telegram
    # menu = driver.find_elements(By.XPATH, '//*[@id="LeftMainHeader"]/div[1]/button')
    # menu[0].click()
    # settings = driver.find_elements(By.XPATH, '//*[@id="LeftMainHeader"]/div[1]/div/div[2]/div[4]')
    # settings[0].click()
    # logout = driver.find_elements(By.XPATH,'//*[@id="Settings"]/div[1]/div[1]/div/div/button')
    # time.sleep(4)
    # print(logout)
    # logout1 = logout[0].find_elements(By.XPATH, '//*[@id="Settings"]/div[1]/div[1]/div/div/div/div[2]/div')
    # print(logout1)
    # logout1.click()
    # time.sleep(10)
    # print(logout)

    # i = i+1  //*[@id="Settings"]/div[1]/div[1]/div/div/button/div  //*[@id="Settings"]/div[1]/div[1]/div/div/button/div
# print(Search)

driver.close()

# //*[@id="telegram-search-input"]   //*[@id="Settings"]/div[1]/div[1]/div/div/button
# //*[@id="LeftMainHeader"]/div[1]/button
# //*[@id="Settings"]/div[1]/div[1]/div/div/button/div
