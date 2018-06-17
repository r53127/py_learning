# -*- coding: utf-8 -*-

"""
Module implementing dish_form.
"""
import sys
from PyQt5.QtCore import pyqtSlot,QRegExp,Qt
from PyQt5.QtWidgets import QWidget,QApplication,QMessageBox,QFileDialog,QComboBox
from PyQt5.QtGui import  QRegExpValidator
from operate_hotel_json import hotel_json
from create_dish_xml import create_xml
from Ui_dish5 import Ui_Form
import random,os
from lxml import etree
import win32api
from hotel_form import hotel_Dialog


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


        #初始化酒店子窗口
        self.hotelDialog=hotel_Dialog()
        #子窗口返回时接受信号，刷新酒店列表
        self.hotelDialog.update_hotel_Signal.connect(self.update_combox)

        #输入金额数字校验
        regx = QRegExp(r'[\d]+')
        validator = QRegExpValidator(regx, self.lineEdit)
        self.lineEdit.setValidator(validator)

        # 酒店下拉列表初始化
        hotel_json_object=hotel_json()
        hotel_info=hotel_json_object.read_data()
        for x in hotel_info:
            y = x['hotel_name']
            self.comboBox.addItem(y)
        self.comboBox.setEditable(True)

    #刷新酒店列表槽函数
    def update_combox(self,str):
        if self.comboBox.findText(str) == -1:
            self.comboBox.insertItem(0,str)

    #生成随机时间函数
    def generate_time(self, account_tmp):
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


    #识别是否是pyinstaller打包文件
    def identify_bundle(self,filename_tmp):
        if getattr(sys, 'frozen', False):
            filename_tmp = os.path.join(sys._MEIPASS, filename_tmp)
        return filename_tmp

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
        xsl_filename=self.comboBox_2.currentText()
        if sum_input=='':
            QMessageBox.information(None,'错误','金额不能为零！')
            return
        if xsl_filename == '':
            QMessageBox.information(None, '错误', '模板不能为空！')
            return
        meal_account = int(sum_input)
        if meal_account <= 500:
            meal_type = '午餐'
        else:
            meal_type = '晚餐'
        meal_time = print_date[0:4] + '-' + print_date[4:6] + '-' + print_date[6:8] + ' ' + self.generate_time(meal_account)

        #随机生成菜单xml文件
        xml_filename = 'dish_menu.xml'
        dish_xml = create_xml(hotel_name, meal_time, meal_account, meal_type)
        menu_filename='dish_menu.txt'
        menu_filename=self.identify_bundle(menu_filename)
        xml_tmp = dish_xml.create(menu_filename)
        dish_xml.write_xml(xml_tmp, xml_filename)

        # xsl_filename = "dish_print1.xsl"
        # xsl_filename=self.identify_bundle(xsl_filename)
        # if not os.path.exists(xsl_filename):
        #     return
        #生成格式化后的html文件
        html_filename = 'dish.html'
    # try:
        xml_dom = etree.parse(xml_filename)
        xsl_dom = etree.parse(xsl_filename)
        # print(xsl_dom)

        transform = etree.XSLT(xsl_dom)
        html_doc = transform(xml_dom)

        fo = open(html_filename, "w", encoding='UTF-8')
        fo.write(str(html_doc))
        fo.close()
        win32api.ShellExecute(0, 'open', html_filename, '', '', 1)
    # except BaseException as e:
    #     print('错误是:',e)
    # else:
        return

    @pyqtSlot(int)
    def on_checkBox_stateChanged(self, p0):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        #显示酒店信息子窗口
        if self.checkBox.checkState()==Qt.Checked:
            hotelname=self.comboBox.currentText()
            if hotelname:
                hotel = hotel_json()
                result=hotel.check_hotel_data(hotelname)
                if result!=False:
                    self.hotelDialog.set_hotelname(*result)
                else:
                    self.hotelDialog.set_hotelname(hotelname)
                self.hotelDialog.exec_()
            else:
                QMessageBox.information(self,'提示','名称不能为空！')

    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        #选择模板文件
        xsl_filename,filetype=QFileDialog.getOpenFileName(self,'打开模板文件',r'.',r'xsl模板文件 (*.xsl)')
        if xsl_filename:
            self.comboBox_2.addItem(xsl_filename)
            self.comboBox_2.setCurrentText(xsl_filename)
        else:
            QMessageBox.information(self, '提示', '请选择打印模板！')


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=dish_form()
    form.show()
    sys.exit(app.exec_())
    

