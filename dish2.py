# coding=UTF-8
import linecache
# linecache只能读取UTF-8文件
from typing import Any, Union

from lxml import etree
import random
import re
# import time
import win32api
# import win32print
import os
import json


# 生成菜价
def generate_item_price(item):
    if  re.search('[\u523A][\u8EAB]|[\u9F99][\u867E]|[\u53C2]', item) :  # 刺身|龙虾|参
        item_price_tmp = random.randrange(200, 300)
    elif re.search('[\u867E\u87F9\u9C7F\u6591\u9E3D]', item) :  # 虾蟹鱿石斑鸽
        item_price_tmp = random.randrange(150, 200)
    elif re.search('[\u9E21\u725B\u9C7C\u6392\u7B19\u868C\u84B8\u7F8A\u9E2D]', item) :  # 鱼鸡牛排骨笙蚌蒸羊鸭
        item_price_tmp = random.randrange(100, 150)
    elif re.search('[\u87F9]|[\u5927][\u867E]', item) :  # 蟹|大虾
        item_price_tmp = random.randrange(100, 200)
    elif re.search('[\u996D]', item) :  # 饭
        item_price_tmp = random.randrange(30, 50)
    else:
        item_price_tmp = random.randrange(60, 90)
    return item_price_tmp


# 盘菜
def generate_dish(item_tmp, item_price_tmp):
    xml_str = ''
    xml_str = xml_str + "<dish><dish_name>" + item_tmp + "</dish_name>"
    xml_str = xml_str + "<dish_num>1</dish_num>"
    xml_str = xml_str + "<dish_price>" + str(item_price_tmp) + ".00</dish_price>"
    xml_str = xml_str + "<dish_account>" + str(item_price_tmp) + ".00</dish_account></dish>" + "\n"
    return xml_str


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


dish_file = 'dish_menu.txt'
while not os.path.exists(dish_file):
    print("请把菜谱文件命名为dish_menu.txt并和程序放在一起再继续...")
    os.system('pause')

hotelname = input("请输入酒店名：")
while not re.match(r'\w+', hotelname):
    hotelname = input("请输入正确的酒店名：")

json_filename='hotel_info.json'
f=open(json_filename,'r')
hotel_info=json.load(f)
for x in hotel_info:
    y=x['hotel_name']
    if y.find(hotelname) == -1:
        find_tag = False
        continue
    else:
        find_tag=True
        break

if not find_tag:
    hotel_flag = input("是否要输入酒店信息：Y/N ? ")
    while not re.match(r'^[YyNn]$', hotel_flag):
        hotel_flag = input("是否要输入酒店信息：Y/N ? ")
    hotel_tmp = []
    if re.match(r'[yY]', hotel_flag):
        hotel_address = input("请输入酒店地址：")
        hotel_phone = input("请输入酒店电话：")
        hotel_data = {r'hotel_name': hotelname, r'hotel_address': hotel_address, r"hotel_phone": hotel_phone}
        if not os.path.exists(json_filename):
            f = open(json_filename, 'w+')
        else:
            f = open(json_filename,'r')
        if f.read() == '':
            hotel_tmp.append(hotel_data)
        else:
            f.close()  # 文件一定要先关闭，因为if判断的时候文件指针已指到最后
            f = open(json_filename, 'r')
            hotel_tmp = json.load(f)
            hotel_tmp.append(hotel_data)
            f.close()
        with open(json_filename, 'w') as f:
            json.dump(hotel_tmp, f, ensure_ascii=False)

print_date = input('请输入打印时间（如20171201)：')
while not re.match(r'^201[\d](0[1-9]|1[0-2])(0[1-9]|1[\d]|2[\d]|3[0-1])$', print_date):
    print_date = input('请输入正确的打印时间（如20171201)：')

sum_input = input('请输入用餐金额：')
while not re.match(r'[\d]+', sum_input):
    sum_input = input('请输入正确的金额：')

account = int(sum_input)
filename = 'dish_menu.xml'
xml_tmp = '<?xml version="1.0" encoding="utf-8"?> \n'

if account <= 500:
    meal_type = '午餐'
else:
    meal_type = '晚餐'

meal_time = print_date[0:4] + '-' + print_date[4:6] + '-' + print_date[6:8] + ' ' + generate_time(account)

xml_tmp = xml_tmp + "<dish_menu hotel_name=\"" + hotelname + "\""
xml_tmp = xml_tmp + " meal_time=\"" + meal_time + "\""
xml_tmp = xml_tmp + " meal_account=\"" + sum_input + ".00\""
xml_tmp = xml_tmp + " meal_type=\"" + meal_type + "\">" + "\n"

item_list = []
dish_sum = 0
lines = len(open(dish_file, encoding='UTF-8').readlines())
xml_content = ''

while dish_sum < account:  # 未达到总金额一直循环
    a = random.randrange(1, lines)  # 随机盘菜
    # 从文件中对读取第a行的菜名
    theline = linecache.getline(dish_file, a)
    # 匹配中文菜名
    dish_item = re.search("[\u4e00-\u9fa5]+", theline)
    # 如果匹配成功则写入
    if dish_item:
        item = dish_item.group()
        if item not in item_list:
            item_price = generate_item_price(item)
            dish_sum = dish_sum + item_price
            if dish_sum <= account:
                # 如果总金额未达到输入金额则直接写入
                xml_content = xml_content + generate_dish(item, item_price)
            else:
                # 如果总金额超出输入金额则最后一道菜按（输入金额-总计）算
                if account - dish_sum + item_price > 50:
                    xml_content = xml_content + generate_dish(item, account - dish_sum + item_price)
                else:
                    # 如果最后一道菜价小于50则菜名改为"小碟"
                    item_last = '小碟'
                    xml_content = xml_content + generate_dish(item_last, account - dish_sum + item_price)
            item_list.append(item)
        else:
            continue
    else:
        continue

xml_tmp = xml_tmp + xml_content
xml_tmp = xml_tmp + "</dish_menu>"
open(filename, 'w', encoding='UTF-8').write(xml_tmp)

if find_tag or re.match(r'[yY]', hotel_flag):
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

xml_dom = etree.parse(filename)
xsl_dom = etree.parse(xsl_filename)

transform = etree.XSLT(xsl_dom)
html_doc = transform(xml_dom)

fo = open(html_filename, "w", encoding='UTF-8')
fo.write(str(html_doc))
fo.close()

win32api.ShellExecute(0, 'open', html_filename, '', '', 1)
