#coding=utf-8

from create_dish_xml import create_xml
from operate_hotel_json import hotel_json
import re
import random
import os
from lxml import etree
import win32api


def generate_time(account_tmp):
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

hotel_name = input("请输入酒店名：")
while not re.match(r'\w+', hotel_name):
    hotel_name = input("请输入正确的酒店名：")

hotel = hotel_json()
check_flag = hotel.check_hotel_data(hotel_name)
hotel_address=''
hotel_phone=''
if check_flag == False:
    hotel_flag = input("是否要输入酒店信息：Y/N ? ")
    while not re.match(r'^[YyNn]$', hotel_flag):
        hotel_flag = input("是否要输入酒店信息：Y/N ? ")
    if re.match(r'[yY]', hotel_flag):
        hotel_address = input("请输入酒店地址：")
        hotel_phone = input("请输入酒店电话：")
        hotel.append_hotel_data(hotel_name, hotel_address, hotel_phone)

print_date = input('请输入打印时间（如20171201)：')
while not re.match(r'^201[\d](0[1-9]|1[0-2])(0[1-9]|1[\d]|2[\d]|3[0-1])$', print_date):
    print_date = input('请输入正确的打印时间（如20171201)：')

sum_input = input('请输入用餐金额：')
while not re.match(r'[\d]+', sum_input):
    sum_input = input('请输入正确的金额：')

meal_account = int(sum_input)

if meal_account <= 500:
    meal_type = '午餐'
else:
    meal_type = '晚餐'

meal_time = print_date[0:4] + '-' + print_date[4:6] + '-' + print_date[6:8] + ' ' + generate_time(meal_account)

xml_filename = 'dish_menu.xml'
dish_xml=create_xml(hotel_name, meal_time, meal_account, meal_type,hotel_address,hotel_phone)
xml_tmp=dish_xml.create('dish_menu.txt')
dish_xml.write_xml(xml_tmp,xml_filename)


if check_flag or re.match(r'[yY]', hotel_flag):
    xsl_filename = "dish_print1.xsl"
    while not os.path.exists(xsl_filename):
        print("请把格式文件命名为dish_print1.xsl并和程序放在一起再继续...")
        os.system('pause')
else:
    xsl_filename="dish_print2.xsl"
    while not os.path.exists(xsl_filename):
        print("请把格式文件命名为dish_print2.xsl并和程序放在一起再继续...")
        os.system('pause')

html_filename = 'dish.html'
xml_dom = etree.parse(xml_filename)
xsl_dom = etree.parse(xsl_filename)

transform = etree.XSLT(xsl_dom)
html_doc = transform(xml_dom)

fo = open(html_filename, "w", encoding='UTF-8')
fo.write(str(html_doc))
fo.close()

win32api.ShellExecute(0, 'open', html_filename, '', '', 1)
