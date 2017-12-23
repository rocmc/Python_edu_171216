#coding: euc-kr

import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QLabel, QApplication, QMainWindow)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # 가로 슬라이더 생성
        self.slider = QSlider(Qt.Horizontal, self)  # 가로 슬라이더 생성
        self.slider.setMaximum(1000)                # 0~1000 사이의 값 선택
        self.slider.setMinimum(0)

        # 위치와 크기
        self.slider.setGeometry(30, 40, 100, 30)

        # 시그널(이벤트) 연결
        self.slider.valueChanged[int].connect(self.changeValue)
        # Qt 슬라이더는 int 값을 가지며, 슬라이더를 움직이면 valueChanged 이벤트가 발생한다.

        # 라벨 생성
        self.label = QLabel("current : 0", self)
        self.label.setGeometry(30,70, 100, 30)

        # 윈도우 위치
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Slider Example')
        self.show()


    def changeValue(self, value):
        "슬라이더 값 출력"
        self.label.setText("current : {}".format(value))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())



