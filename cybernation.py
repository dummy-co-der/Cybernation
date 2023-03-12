import os
import json
import sys
import time
import pandas as pd
from selenium import webdriver
from tkinter import filedialog
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class bluk_message:

	services = {

		'whatsapp' : {
			'link' : 'https://web.whatsapp.com',
			'search' : '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]',
			'message' : '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]',
			'box' : '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span',
			'image_box': '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]',
			'image_send' : '//span[@data-icon="send"]',
			'first' : '//*[@id="app"]/div/div/div[3]/header/div[2]/div/span/div[4]/div/span',
			'second' : '//*[@id="app"]/div/div/div[3]/header/div[2]/div/span/div[4]/span/div/ul/li[6]',
			'thrid': '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[3]/div/div[2]/div/div"]'
		}, 

		'telegram' : {
			'link' : 'https://webogram.org/z/',
			'search' : '//*[@id="telegram-search-input"]',
			'message' : '/html/body/div[1]/div/div/div/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[1]'
		}, 

		'instagram' : {
			'link' : 'https://www.instagram.com/',
			'first_input' : '//*[@id="loginForm"]/div/div[1]/div/label/input',
			'second_input' : '//*[@id="loginForm"]/div/div[2]/div/label/input', 
			'thrid_button' : '//*[@id="loginForm"]/div/div[3]/button', 
			'forth_button' : '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button', 
			'message' : '//*[@id="editable-message-text"]',
			'search' : '//*[@id="telegram-search-input"]',
			'message' : '//*[@id="editable-message-text"]'
		}

	} 

	def __init__(self):
		self.filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
		os.environ['PATH'] += "E:"
		self.driver = webdriver.Chrome() 

	def whatsapp(self):

		df = pd.read_csv(str(self.filename))
		self.Name = df['Name'].tolist()
		self.Number = df["MobileNo"].tolist() 
		self.Message = df["Message"].tolist()  
		self.Image = df["whatsapp_image"].tolist()  

		self.driver.get(str(self.services["whatsapp"]["link"]))
		time.sleep(20)
		for x,y,z,m in zip(self.Name, self.Message, self.Number, self.Image): 
			Search = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,str(self.services["whatsapp"]["search"]))))
			time.sleep(2)
			Search.send_keys(z)
			time.sleep(2)
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
				time.sleep(5)
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
				time.sleep(5)  
			else: 
				continue 

		#logout
		logout = self.driver.find_elements(By.XPATH,str(self.services["whatsapp"]["first"]))
		logout[0].click()
		time.sleep(5)
		logout_div = self.driver.find_elements(By.XPATH,str(self.services["whatsapp"]["second"]))
		logout_div[0].click()  
		time.sleep(5)
		logout_button = self.driver.find_elements(By.XPATH,str(self.services["whatsapp"]["thrid"]))
		logout_button[0].click()
		time.sleep(20)


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

	def insta(self):

		self.driver.get(str(self.services["instagram"]["link"]))
		time.sleep(1)
		f = open('ceredentials.json')
		data = json.load(f) 

		if (data['ceredentials'][0]['gmail'] == "Null"): 
			username_input = self.driver.find_elements(By.XPATH,str(self.services["instagram"]["first_input"]))
			username_input[0].send_keys(data['ceredentials'][0]['username']) 
		else:
			usergmail_input = self.driver.find_elements(By.XPATH,str(self.services["instagram"]["first_input"]))
			usergmail_input[0].send_keys(data['ceredentials'][0]['gmail']) 
		
		userpassword_input = self.driver.find_elements(By.XPATH,str(self.services["instagram"]["second_input"]))
		userpassword_input[0].send_keys(data['ceredentials'][0]['password'])   
		login_button = self.driver.find_elements(By.XPATH,str(self.services["instagram"]["thrid_button"])) 
		print(login_button)
		login_button[0].click()




		
