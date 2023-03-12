import sys
from cybernation import bluk_message
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QFileDialog


class work(QMainWindow):
	def __init__(self):
		super(work, self).__init__()
		label = QLabel(self)
		pixmap = QPixmap('images/background.jpg')
		label.setPixmap(pixmap)
		self.setCentralWidget(label)
		self.resize(pixmap.width(), pixmap.height())
		self.setGeometry(100, 100, 900, 800)
		self.setWindowTitle("Cybernation")
		self.initUI()

	def initUI(self):

		self.b1 = QtWidgets.QPushButton(self)
		self.b1.setText(" WhatsApp")
		self.b1.setFont(QFont('Times', 15))
		self.b1.setGeometry(210, 300, 180, 50)
		self.b1.setStyleSheet("background-color : Green")
		self.b1.setIcon(QIcon('images/whatsapp.png'))
		self.b1.clicked.connect(self.whatsapp)

		self.b2 = QtWidgets.QPushButton(self)
		self.b2.setText(" Telegram")
		self.b2.setFont(QFont('Times', 15))
		self.b2.setGeometry(210, 400, 180, 50)
		self.b2.setStyleSheet("background-color : cyan")
		self.b2.setIcon(QIcon('images/tele.png'))
		#self.b2.clicked.connect(self.tele)

		self.b3 = QtWidgets.QPushButton(self)
		self.b3.setText(" Instagram")
		self.b3.setFont(QFont('Times', 15))
		self.b3.setGeometry(210, 500, 180, 50)
		self.b3.setStyleSheet("background-color : pink")
		self.b3.setIcon(QIcon('images/instagram.png'))
		#self.b3.clicked.connect(self.insta)

		self.b4 = QtWidgets.QPushButton(self)
		self.b4.setText(" Exit")
		self.b4.setFont(QFont('Times', 15))
		self.b4.setGeometry(1000, 650, 180, 50)
		self.b4.setStyleSheet("background-color : white")
		self.b4.setIcon(QIcon('images/exit.png'))
		self.b4.clicked.connect(self.exiti)

	def whatsapp(self):
		obj = bluk_message()
		obj.whatsapp()

	def exiti(self):
   		self.close()

   	#def tele(self):
		#obj = bluk_message()  
		#obj.telegram()

	#def insta(self):
		#obj = bluk_message()  
		#obj.insta()


def window():
	app = QApplication(sys.argv) #application setup
	win = work()
	win.show()
	sys.exit(app.exec_()) 

window()