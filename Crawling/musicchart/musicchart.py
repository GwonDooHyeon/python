# 음원 차트 조회 앱

# 윈도우 기본창 띄우기 

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver # 위에서 requests랑은 다른 것
import time

form_class = uic.loadUiType("musicchart.ui")[0]

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 단추를 누르면
        self.bugsButton.clicked.connect(self.bugsbtnclicked)
        self.melonButton.clicked.connect(self.melonbtnclicked)
        self.genieButton.clicked.connect(self.geniebtnclicked)


        # 조회 후 칸에 출력
# 벅스
    def bugsbtnclicked(self):
        
        self.label.setText("Bugs 차트 100")
        self.tableWidget.clear()

        url = "https://music.bugs.co.kr/chart"
        txt = requests.get(url)
        html = bs(txt.text)

        songs = html.select('table.byChart > tbody > tr')
                                  
        for i, song in enumerate(songs):
                
            title = song.select('p.title > a')[0].text
            singer = song.select('p.artist > a')[0].text   
            self.tableWidget.setItem(i, 0, QTableWidgetItem('Bugs'))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(title))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(singer))

# 멜론
    def melonbtnclicked(self):
        
        self.label.setText("Melon 차트 100")
        self.tableWidget.clear()

        driver = webdriver.Chrome('chromedriver.exe')
        driver.get("https://www.melon.com/chart/")

        txt = driver.page_source
        html = bs(txt)

        songs = html.select('tbody > tr')
                                  
        for i, song in enumerate(songs):
                
            title = song.select('.rank01 > span > a')[0].text
            singer = song.select('.rank02 > span > a')[0].text
            self.tableWidget.setItem(i, 0, QTableWidgetItem('Melon'))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(title))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(singer))

# 지니
    def geniebtnclicked(self):
        
        self.label.setText("Genie 차트 100")
        self.tableWidget.clear()

        driver = webdriver.Chrome('chromedriver.exe')
        url = "https://www.genie.co.kr/chart/top200"
        driver.get(url)

        txt = driver.page_source
        html = bs(txt)

        songs = html.select('tbody > tr')
                                  
        for i, song in enumerate(songs):
                
            title = song.select('a.title')[0].text.strip()
            singer = song.select('a.artist')[0].text.strip() 
            self.tableWidget.setItem(i, 0, QTableWidgetItem('Genie'))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(title))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(singer))

        time.sleep(1)
        url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20230228&hh=14&rtm=Y&pg=2'
        driver.get(url)

        txt = driver.page_source      # 이때 읽어온 데이터는 그냥 글자
        html = bs(txt)

        songs = html.select('tbody > tr')
        
        for i, song in enumerate(songs):
                
            title = song.select('a.title')[0].text.strip()
            singer = song.select('a.artist')[0].text.strip() 
            self.tableWidget.setItem(i+50, 0, QTableWidgetItem('Genie'))
            self.tableWidget.setItem(i+50, 1, QTableWidgetItem(title))
            self.tableWidget.setItem(i+50, 2, QTableWidgetItem(singer))
           
   
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()