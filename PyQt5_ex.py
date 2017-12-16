# #coding: euc-kr

# import sys
# from PyQt5.Qt\idgets import *
#
# app = QApplication(sys.argv)
# label + QLabel("Hello PyQt")
# label.show()
# app.exec_()
#



import sys

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication)

app = QApplication([])
dialog = QInputDialog()
dialog.show()
app.exec_()

