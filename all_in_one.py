from tkinter import *
from tkinter import filedialog
from tkinter import ttk 
import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd

class bluk_message:

	filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
	os.environ['PATH'] += "E:"
	driver = webdriver.Chrome() 

	services = {

		'whatsapp' : {
			'link' : 'https://web.whatsapp.com',
			'search' : '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]',
			'message' : '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]',
			'box' : '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span',
			'image_box': '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]',
			'image_send' : '//span[@data-icon="send"]'
		}, 

		'telegram' : {
			'link' : 'https://webogram.org/z/',
			'search' : '//*[@id="telegram-search-input"]',
			'message' : '/html/body/div[1]/div/div/div/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[1]'
		}, 

		'messanger' : {
			'link' : 'https://web.whatsapp.com',
			'search' : '//*[@id="telegram-search-input"]',
			'message' : '//*[@id="editable-message-text"]'
		}, 

		'snapchat' : {
			'link' : 'https://web.whatsapp.com',
			'search' : '//*[@id="telegram-search-input"]',
			'message' : '//*[@id="editable-message-text"]'
		}, 

		'linkedIn' : {
			'link' : 'https://web.whatsapp.com',
			'search' : '//*[@id="telegram-search-input"]',
			'message' : '//*[@id="editable-message-text"]'
		} 

	} 

	def __init__(self, option):
		self.option = option 

	def scrapdata(self): 

		df = pd.read_csv(str(self.filename))
		self.Name = df['Name'].tolist()
		self.Number = df["MobileNo"].tolist() 
		self.Message = df["Message"].tolist()  
		self.Image = df["whatsapp_image"].tolist()   

	def printme(self):

		print(self.Name)
		print(self.Number)
		print(self.Message)  


	def whatsapp(self):

		self.driver.get(str(self.services["whatsapp"]["link"]))
		time.sleep(10)
		for x,y,z,m in zip(self.Name, self.Message, self.Number, self.Image): 
			Search = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,str(self.services["whatsapp"]["search"]))))
			time.sleep(2)
			Search.send_keys(z)
			time.sleep(1)
			Search.send_keys(Keys.ENTER)
			time.sleep(3)
			Message = self.driver.find_elements(By.XPATH,str(self.services["whatsapp"]["message"]))
			time.sleep(2)  

			if y != None:
				Message[0].send_keys('Hello ' + str(x)+ ',')
				time.sleep(1)
				Message[0].send_keys(Keys.SHIFT, Keys.ENTER)
				Message[0].send_keys(Keys.SHIFT, Keys.ENTER)
				Message[0].send_keys(str(y))
				time.sleep(1)
				Message[0].send_keys(Keys.ENTER)   
				time.sleep(10)
			else: 
				continue 

			#image
			if m != None:
				box = self.driver.find_elements(By.XPATH,str(self.services["whatsapp"]["box"]))  
				box[0].click()
				img_box = self.driver.find_elements(By.XPATH,str(self.services["whatsapp"]["image_box"]))
				img_box[0].send_keys(m) 
				time.sleep(2) 
				send_button = self.driver.find_elements(By.XPATH,str(self.services["whatsapp"]["image_send"])) 
				send_button[0].click() 
				time.sleep(10)  
			else: 
				continue

	def telegram(self):

		self.driver.get(str(self.services["telegram"]["link"]))
		time.sleep(10)
		for x,y,m in zip(self.Name, self.Message, self.Image): 
			Search = self.driver.find_elements(By.XPATH,str(self.services["telegram"]["search"]))
			time.sleep(2) 
			print(Search)
			Search.send_keys(x)
			time.sleep(1)
			Search.send_keys(Keys.ENTER)
			time.sleep(3)
			Message = self.driver.find_elements(By.XPATH,str(self.services["telegram"]["message"]))
			time.sleep(2)  
			print(Message)

			if y != None:
				Message[0].send_keys('Hello ' + str(x)+ ',')
				time.sleep(1000)
				Message[0].send_keys(Keys.SHIFT, Keys.ENTER)
				Message[0].send_keys(Keys.SHIFT, Keys.ENTER)
				Message[0].send_keys(str(y))
				time.sleep(1)
				Message[0].send_keys(Keys.ENTER)   
				time.sleep(10)
			else:  
				continue 

			


obj = bluk_message('whatsapp') 
obj.scrapdata() 
obj.whatsapp()


#//*[@id="LeftColumn-main"]/div[2]/div[2]/div/div[2]/div/div/div/h3
#//*[@id="LeftColumn-main"]/div[2]/div[2]/div/div[2]/div/div/div/div[1]


#//*[@id="LeftColumn-main"]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div/div
#//*[@id="LeftColumn-main"]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div/div/div[2]
#//*[@id="LeftColumn-main"]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div/div/div[2]/span
#//*[@id="LeftColumn-main"]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div/div/div[2]/span/span[1]
