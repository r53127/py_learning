# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\py_learning\dish5.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class myComboBox(QtWidgets.QComboBox):
    def focusOutEvent(self, QFocusEvent):
        print('激活focusout')

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(396, 312)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 40, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 72, 15))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(110, 150, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(70, 230, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 230, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = myComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(110, 30, 211, 31))
        self.comboBox.setObjectName("comboBox")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(110, 90, 211, 31))
        self.dateEdit.setProperty("showGroupSeparator", False)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.label.setBuddy(self.comboBox)
        self.label_2.setBuddy(self.dateEdit)
        self.label_3.setBuddy(self.lineEdit)

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.comboBox, self.lineEdit)
        Form.setTabOrder(self.lineEdit, self.pushButton)
        Form.setTabOrder(self.pushButton, self.pushButton_2)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "dish5"))
        self.label.setText(_translate("Form", "酒店名称："))
        self.label_2.setText(_translate("Form", "消费时间："))
        self.label_3.setText(_translate("Form", "消费金额"))
        self.pushButton.setText(_translate("Form", "打印"))
        self.pushButton_2.setText(_translate("Form", "退出"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

