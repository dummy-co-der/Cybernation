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
driver.get('https://www.instagram.com/')
time.sleep(50)
# df = pd.read_csv("workbook.csv")
# Name = df["Name"].tolist()
# Message = df["Message"].tolist()
# for x, y in zip(Name, Message):
Search = driver.find_elements(By.XPATH, '')
time.sleep(2)
# Username - string sensitive
# Search[0].send_keys(x)
# time.sleep(1)
# Search[0].send_keys(Keys.ENTER)
# # time.sleep(3)
# message = driver.find_elements(By.XPATH, '')
#     message[0].send_keys(y)
#     message[0].send_keys(Keys.ENTER)
#     time.sleep(4)