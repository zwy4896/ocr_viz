import sys
import os
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('reader_viz')
        self.setWindowIcon(QIcon('./res/logo.jpg'))

        fileOpen = QAction(QIcon(), '&Open', self)
        fileOpen.setShortcut('Ctrl+O')
        fileOpen.setStatusTip('Exit application')
        fileOpen.triggered.connect(self.openFile)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(fileOpen)

        self.setGeometry(10, 10, 800, 800)
        # self.setWindowTitle('Simple menu')
        # self.show()

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
 
        fh = ''
        print(filename, _)
 
        # if QFile.exists(filename):
        #     fh = QFile(filename)
 
        # if not fh.open(QFile.ReadOnly):
        #     qApp.quit()

        # data = fh.readAll()
        # codec = QTextCodec.codecForUtfText(data)
        # unistr = codec.toUnicode(data)
 
        # tmp = ('%s' % filename)
        # self.setWindowTitle(tmp)

def main():
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()