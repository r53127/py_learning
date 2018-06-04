from PyQt5 import QtGui, QtCore,QtWidgets
from PyQt5.QtWidgets import QApplication,QMessageBox,QPushButton
from PyQt5.QtCore import pyqtSignal

app = QApplication([])

w = QtWidgets()

def showMsg():
    QMessageBox.information(w, u"信息", u"ok")

btn = QPushButton(u"点我", w)
w.connect(btn, SIGNAL("clicked()"), showMsg)

w.show()
app.exec_()