# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication,QFileDialog,QCalendarWidget
from operate_hotel_json import hotel_json
from Ui_dish5 import Ui_Form


class Form(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(Form, self).__init__(parent)
        self.setupUi(self)

        hotel_json_object=hotel_json()
        hotel_info=hotel_json_object.read_data()
        for x in hotel_info:
            y = x['hotel_name']
            self.comboBox.addItem(y)
        self.comboBox.setEditable(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = Form()
    Form.show()
    sys.exit(app.exec_())



