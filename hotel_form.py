# -*- coding: utf-8 -*-

"""
Module implementing hotel_Dialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog,QMessageBox
from operate_hotel_json import hotel_json
from Ui_hotel_form import Ui_Dialog



class hotel_Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(hotel_Dialog, self).__init__(parent)
        self.setupUi(self)

    def set_hotelname(self,hotelname):
        self.lineEdit_3.setText(hotelname)
        self.lineEdit_3.setReadOnly(True)

    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        hotelname = self.lineEdit_3.text()
        hoteladdress = self.lineEdit.text()
        hotelphone = self.lineEdit_2.text()
        # print(hotelname,hoteladdress,hotelphone)
        hotel = hotel_json()
        if not hotel.check_hotel_data(hotelname):
            hotel.append_hotel_data(hotelname, hoteladdress, hotelphone)
            self.close()
        else:
            # print('已存在')
            QMessageBox.information(None, '提示', '酒店已存在！')

