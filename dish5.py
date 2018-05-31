# -*- coding: utf-8 -*-

"""
Module implementing dish_form.
"""
import sys
from PyQt5.QtCore import pyqtSlot,QRegExp
from PyQt5.QtWidgets import QWidget,QApplication,QMessageBox
from PyQt5.QtGui import  QRegExpValidator
from operate_hotel_json import hotel_json
from create_dish_xml import create_xml
from Ui_dish5 import Ui_Form
import random
from lxml import etree
import win32api

class dish_form(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(dish_form, self).__init__(parent)
        self.setupUi(self)

        regx = QRegExp(r'[\d]+')
        validator = QRegExpValidator(regx, self.lineEdit)
        self.lineEdit.setValidator(validator)

        # self.lineEdit.editingFinished.connect(self.onChanged)
        hotel_json_object=hotel_json()
        hotel_info=hotel_json_object.read_data()
        for x in hotel_info:
            y = x['hotel_name']
            self.comboBox.addItem(y)
        self.comboBox.setEditable(True)
        self.comboBox.currentIndexChanged.connect(self.on_combobox_changed)



    def on_combobox_changed(self):
        print('aaaa')

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        hotel_name=self.comboBox.currentText()
        selected_date=self.dateEdit.date()
        print_date=selected_date.toString("yyyyMMdd")
        sum_input=self.lineEdit.text()
        meal_account = int(sum_input)
        if meal_account <= 500:
            meal_type = '午餐'
        else:
            meal_type = '晚餐'
        meal_time = print_date[0:4] + '-' + print_date[4:6] + '-' + print_date[6:8] + ' ' + self.generate_time(meal_account)

        xml_filename = 'dish_menu.xml'
        dish_xml = create_xml(hotel_name, meal_time, meal_account, meal_type)
        xml_tmp = dish_xml.create('dish_menu.txt')
        dish_xml.write_xml(xml_tmp, xml_filename)

        xsl_filename = "dish_print1.xsl"
        html_filename = 'dish.html'
        xml_dom = etree.parse(xml_filename)
        xsl_dom = etree.parse(xsl_filename)

        transform = etree.XSLT(xsl_dom)
        html_doc = transform(xml_dom)

        fo = open(html_filename, "w", encoding='UTF-8')
        fo.write(str(html_doc))
        fo.close()
        win32api.ShellExecute(0, 'open', html_filename, '', '', 1)

    def generate_time(self,account_tmp):
        if account_tmp < 500:
            h = random.randrange(13, 15)
            m = random.randrange(0, 60)
            s = random.randrange(0, 60)
        else:
            h = random.randrange(19, 23)
            m = random.randrange(0, 60)
            s = random.randrange(0, 60)
        time_tmp = str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2)
        return time_tmp

    @pyqtSlot(str)
    def on_lineEdit_textChanged(self, p0):
        print('adfasdfasdf')
        QMessageBox.information(self,'不合格','pls reedit')

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=dish_form()
    form.show()
    sys.exit(app.exec_())
    

