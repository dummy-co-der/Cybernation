from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
import pywhatkit as py

window = Tk() 

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    os.environ['PATH'] += "E:"
    driver = webdriver.Chrome() 
    driver.get('https://web.whatsapp.com')
    time.sleep(25)
    df = pd.read_csv(str(filename))
    Name = df['Name'].tolist()
    Number = df["MobileNo"].tolist() 
    Message = df["Message"].tolist()
    for i,j,l in zip(Number, Name, Message):
        Search = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')))
        time.sleep(2)
        Search.send_keys(i)
        time.sleep(1)
        Search.send_keys(Keys.ENTER)
        time.sleep(3)
        Message = driver.find_elements(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
        time.sleep(2)
        
        #message
        if l != None:
            Message[0].send_keys('Hello ' + str(j)+ ',')

            time.sleep(1)
            Message[0].send_keys(Keys.SHIFT, Keys.ENTER)
            Message[0].send_keys(Keys.SHIFT, Keys.ENTER)
            Message[0].send_keys(str(l))
            time.sleep(1)
            Message[0].send_keys(Keys.ENTER)  
        else: 
            continue

        print('Sent to ' + str(j))
    
    Logout = driver.find_elements(By.XPATH,'//*[@id="app"]/div/div/div[3]/header/div[2]/div/span/div[4]/div/span') 
    Logout[0].find_elements(By.XPATH,'//*[@id="app"]/div/div/div[3]/header/div[2]/div/span/div[4]/span/div/ul/li[5]/div')
    Logout[0].click()

    driver.close() 
        
        
window.title('Cybernation') 
window.geometry("600x600")
window.config(background = "white")
frmae = LabelFrame(window, text="Cybernation",font=("sans-serif", 25), relief="sunken",background = "light Blue", padx=200, pady=200)
frmae.pack(padx=10, pady=10) 
b1 = Button(frmae,text = "Link Your CSV File Here..",command = browseFiles, fg="blue") 
b2 = Button(frmae,text = "       Exit       ",command = exit, fg="blue")  
b1.grid( row = 0,column = 0)
b2.grid( row = 1,column = 3) 
#b2.pack(side = 'right')
window.mainloop()
