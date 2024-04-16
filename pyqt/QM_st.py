import sys
from PyQt6.QtWidgets import QMainWindow, QApplication,QMenu
from  PyQt6.QtGui import QIcon,QAction
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('状态栏标签')
        exitAct=QAction(QIcon('exit.png'),'&Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(QApplication.instance().quit)
        menubar=self.menuBar()
        fileMenu=menubar.addMenu('&File')
        impMenu=QMenu('Import',self)
        impAct=QAction('Import mail',self)
        impMenu.addAction(impAct)
        newAct=QAction('New',self)
        fileMenu.addAction(newAct)
        fileMenu.addAction(exitAct)
        fileMenu.addMenu(impMenu)
        self.setGeometry(300,300,350,250)
        self.setWindowTitle(' this is statusb')
        self.show()
    def initUI_repeat(self):
        pass
def main():
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec())
if __name__=='__main__':
    main()
