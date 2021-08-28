import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import requests
from bs4 import BeautifulSoup

html = requests.get('https://superkts.com/cal/su_day/2022')
html2 = requests.get('https://search.naver.com/search.naver?sm=tab_sug.top&where=nexearch&query=2022+%EC%88%98%EB%8A%A5+%EB%94%94%EB%8D%B0%EC%9D%B4')

soup = BeautifulSoup(html.text, 'html.parser')
soup2 = BeautifulSoup(html2.text, 'html.parser')

date = soup2.select_one('#main_pack > section.sc_new.cs_suneung._cs_CSAT > div > div.api_cs_wrap > div.sn_box > div > dl > dd:nth-child(2)').text
day = soup.select_one('body > main > section > article.result > b').text






class suneung(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        daylabel1 = QLabel(day, self)
        daylabel1.setAlignment(Qt.AlignCenter)

        label2 = QLabel(date, self)
        label2.setAlignment(Qt.AlignCenter)

        font1 = daylabel1.font()
        font1.setFamily('굴림')
        font1.setPointSize(20)
        font1.setBold(True)


        font2 = label2.font()
        font2.setFamily('굴림')


        daylabel1.setFont(font1)
        label2.setFont(font2)

        layout = QVBoxLayout()
        layout.addWidget(daylabel1)
        layout.addWidget(label2)

        self.setLayout(layout)

        self.setWindowIcon(QIcon('Icon.jfif'))
        self.setWindowTitle('인서울 드가자~')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = suneung()
    sys.exit(app.exec_())