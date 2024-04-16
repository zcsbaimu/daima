import sys
from PyQt6.QtWidgets import QApplication, QWidget, QToolTip, QPushButton,QMessageBox
from PyQt6.QtGui import QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.resize(350,250)
        self.center()
        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('This is a <b>QWidget </b> widget')
        btn=QPushButton('button',self)
        qbtn=QPushButton('Quit',self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(100,50)
        btn.setToolTip('button')
        self.resize(btn.sizeHint())
        btn.move(50,50)
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Tooltips')
        self.show()
    def center(self):
        qr=self.frameGeometry()
        cp=self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def closeEvent(self, event):
        reply=QMessageBox.question(self,'想退出吗','你干嘛',QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No,QMessageBox.StandardButton.No)
        if reply==QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
def main():
    app = QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
