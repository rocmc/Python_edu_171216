#coding: euc-kr

import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QLabel, QApplication, QMainWindow)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # ���� �����̴� ����
        self.slider = QSlider(Qt.Horizontal, self)  # ���� �����̴� ����
        self.slider.setMaximum(1000)                # 0~1000 ������ �� ����
        self.slider.setMinimum(0)

        # ��ġ�� ũ��
        self.slider.setGeometry(30, 40, 100, 30)

        # �ñ׳�(�̺�Ʈ) ����
        self.slider.valueChanged[int].connect(self.changeValue)
        # Qt �����̴��� int ���� ������, �����̴��� �����̸� valueChanged �̺�Ʈ�� �߻��Ѵ�.

        # �� ����
        self.label = QLabel("current : 0", self)
        self.label.setGeometry(30,70, 100, 30)

        # ������ ��ġ
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Slider Example')
        self.show()


    def changeValue(self, value):
        "�����̴� �� ���"
        self.label.setText("current : {}".format(value))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())



