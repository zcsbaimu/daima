#https://maicss.com/pyqt/v6/menusAndToolbars
#V_building_0.1
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication,QMenu
from  PyQt6.QtGui import QIcon,QAction
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.initUI_init()
        viewenu=self.menubar.addMenu('View')
        viewStatAct=QAction('View stausbar',self,checkable=True)

    def initUI_init(self):
        self.statusBar=self.statusBar()
        self.statusBar.showMessage('状态栏标签')
        self.exitAct=QAction(QIcon('exit.png'),'&Exit',self)
        self.exitAct.setShortcut('Ctrl+Q')
        self.exitAct.setStatusTip('Exit application')
        self.exitAct.triggered.connect(QApplication.instance().quit)
        self.menubar=self.menuBar()
        self.fileMenu=self.menubar.addMenu('&File')
        impMenu=QMenu('Import',self)
        impAct=QAction('Import mail',self)
        impMenu.addAction(impAct)
        newAct=QAction('New',self)
        self.fileMenu.addAction(newAct)
        self.fileMenu.addAction(self.exitAct)
        self.fileMenu.addMenu(impMenu)
        self.setGeometry(300,300,350,250)
        self.setWindowTitle(' this is statusb')
        self.show()
def main():
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec())
if __name__=='__main__':
    main()
