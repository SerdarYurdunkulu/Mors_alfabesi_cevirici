import morskodu
from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QApplication,QPushButton,QVBoxLayout,QMainWindow,QLineEdit,QTextEdit,QTextBrowser

class Pencerem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Mors Çevirici")

        self.metinkutusu = QLineEdit(self)
        self.metinkutusu.move(50,65)
        self.metinkutusu.setFixedWidth(200)
        self.metinkutusu.setFixedHeight(30)

        self.metincıktı = QTextBrowser()
        self.metincıktı.move(50,135)
        self.metincıktı.setFixedHeight(200)
        self.metincıktı.setFixedWidth(30)

        self.araclar()

    def araclar(self):
            self.buton = QPushButton(self)
            self.buton.setText("Çevir")
            self.buton.clicked.connect(self.tikla)
            self.buton.move(100,100)

    def tikla(self):
        metin = self.metinkutusu.text()
        morskodu.morscevirivi(metin)



def pencere():
    uygulama = QApplication(sys.argv)
    pencere = Pencerem()
    pencere.show()
    sys.exit(uygulama.exec_())

pencere()