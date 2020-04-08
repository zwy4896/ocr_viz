#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2020/04/07 16:41:53
@Author  :   Zhang Wuyang
@Version :   1.0
'''

# here put the import lib

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.center()

    def initUI(self):
        self.widget = ImageWithMouseControl(self)
        self.setGeometry(10, 10, 1280, 960)
        self.widget.setGeometry(10, 10, 1280, 960)
        self.setWindowTitle('reader_viz')
        self.setWindowIcon(QIcon('./res/logo.jpg'))

        fileOpen = QAction(QIcon(), '&Open', self)
        fileOpen.setShortcut('Ctrl+O')
        fileOpen.setStatusTip('Exit application')
        # fileOpen.triggered.connect(self.openFile)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(fileOpen)

    def center(self):
        screen = QDesktopWidget().screenGeometry() #计算显示屏的尺寸
        size = self.geometry()          #计算qwidget的窗口大小
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)  #把窗口移动到屏幕正中央

class ImageWithMouseControl(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.img = QPixmap('D:\Documents\\!Tools\\reader_vis\\test\\yingyubaozhi30cm_20191212_1.jpg')
        self.scaled_img = self.img.scaled(self.size())
        self.point = QPoint(0, 0)

    def paintEvent(self, e):
        '''
        绘图
        :param e:
        :return:
        '''
        painter = QPainter()
        painter.begin(self)
        self.draw_img(painter)
        painter.end()

    def draw_img(self, painter):
        painter.drawPixmap(self.point, self.scaled_img)

    def mouseMoveEvent(self, e):  # 重写移动事件
        if self.left_click:
            self._endPos = e.pos() - self._startPos
            self.point = self.point + self._endPos
            self._startPos = e.pos()
            self.repaint()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.left_click = True
            self._startPos = e.pos()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.left_click = False
        elif e.button() == Qt.RightButton:
            self.point = QPoint(0, 0)
            self.scaled_img = self.img.scaled(self.size())
            self.repaint()

    def wheelEvent(self, e):
        if e.angleDelta().y() < 0 and (self.scaled_img.height() > 100 and self.scaled_img.width() > 100):
            # 缩小图片
            # print(e.angleDelta().y())
            self.scaled_img = self.img.scaled(self.scaled_img.width() * 0.75, self.scaled_img.height() * 0.75)
            print(self.scaled_img.width(), self.scaled_img.height())
            new_w = e.x() - (self.scaled_img.width() * (e.x() - self.point.x())) / (self.scaled_img.width() + 50)
            new_h = e.y() - (self.scaled_img.height() * (e.y() - self.point.y())) / (self.scaled_img.height() + 50)
            self.point = QPoint(new_w, new_h)
            self.repaint()
        elif e.angleDelta().y() > 0:
            # 放大图片
            print(e.x(), e.y())
            self.scaled_img = self.img.scaled(self.scaled_img.width()*1.25, self.scaled_img.height()*1.25)
            new_w = e.x() - (self.scaled_img.width() * (e.x() - self.point.x())) / (self.scaled_img.width() - 50)
            new_h = e.y() - (self.scaled_img.height() * (e.y() - self.point.y())) / (self.scaled_img.height() - 50)
            self.point = QPoint(new_w, new_h)
            self.repaint()

    def resizeEvent(self, e):
        if self.parent is not None:
            self.scaled_img = self.img.scaled(self.size())
            self.point = QPoint(0, 0)
            self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    # ex = ImageWithMouseControl()
    ex.show()
    app.exec_()