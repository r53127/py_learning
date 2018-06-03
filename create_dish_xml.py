__author__ = 'rnkn@163.com'
'''
Instructions:
Step 1:Init
Step 2:create 
'''

import random
import re
import linecache
import os


class create_xml():
    def __init__(self, hotel_name, meal_time, meal_account, meal_type, hotel_address='', hotel_phone=''):
        self._hotel_name = hotel_name
        self._meal_time = meal_time
        self._meal_account = meal_account
        self._hotel_address = hotel_address
        self._hotel_phone = hotel_phone
        self._meal_type = meal_type

    # 生成菜价
    def __generate_item_price(self, item):
        if re.search('[\u523A][\u8EAB]|[\u9F99][\u867E]|[\u53C2]', item):  # 刺身|龙虾|参
            item_price_tmp = random.randrange(200, 300)
        elif re.search('[\u867E\u87F9\u9C7F\u6591\u9E3D]', item):  # 虾蟹鱿石斑鸽
            item_price_tmp = random.randrange(150, 200)
        elif re.search('[\u9E21\u725B\u9C7C\u6392\u7B19\u868C\u84B8\u7F8A\u9E2D]', item):  # 鱼鸡牛排骨笙蚌蒸羊鸭
            item_price_tmp = random.randrange(100, 150)
        elif re.search('[\u87F9]|[\u5927][\u867E]', item):  # 蟹|大虾
            item_price_tmp = random.randrange(100, 200)
        elif re.search('[\u996D]', item):  # 饭
            item_price_tmp = random.randrange(30, 50)
        else:
            item_price_tmp = random.randrange(60, 90)
        return item_price_tmp

    # 盘菜
    def __generate_dish(self, item_tmp, item_price_tmp):
        xml_str = ''
        xml_str = xml_str + "<dish><dish_name>" + item_tmp + "</dish_name>"
        xml_str = xml_str + "<dish_num>1</dish_num>"
        xml_str = xml_str + "<dish_price>" + str(item_price_tmp) + ".00</dish_price>"
        xml_str = xml_str + "<dish_account>" + str(item_price_tmp) + ".00</dish_account></dish>\n"
        return xml_str

    def create(self, dish_menu_file):
        while not os.path.exists(dish_menu_file):
            print("请传入有效的菜谱txt文件再继续...")
            os.system('pause')
        xml_tmp = '<?xml version="1.0" encoding="utf-8"?>\n'
        xml_tmp = xml_tmp + "<dish_menu hotel_name=\"" + self._hotel_name + "\""
        xml_tmp = xml_tmp + " meal_time=\"" + self._meal_time + "\""
        xml_tmp = xml_tmp + " meal_account=\"" + str(self._meal_account) + ".00\""
        if self._hotel_address != '':
            xml_tmp = xml_tmp + " hotel_address=\"" + self._hotel_address + "\""
            xml_tmp = xml_tmp + " hotel_phone=\"" + self._hotel_phone + "\""
        xml_tmp = xml_tmp + " meal_type=\"" + self._meal_type + "\">\n"

        dish_sum = 0
        xml_body = ''
        item_list = []
        lines = len(open(dish_menu_file, encoding='UTF-8').readlines())
        while dish_sum < self._meal_account:  # 未达到总金额一直循环
            a = random.randrange(1, lines)  # 随机盘菜
            # 从文件中对读取第a行的菜名
            theline = linecache.getline(dish_menu_file, a)
            # 匹配中文菜名
            dish_item = re.search("[\u4e00-\u9fa5]+", theline)
            # 如果匹配成功则写入
            if dish_item:
                item = dish_item.group()
                if item not in item_list:
                    item_list.append(item)
                    item_price = self.__generate_item_price(item)
                    dish_sum = dish_sum + item_price
                    if dish_sum <= self._meal_account:
                        # 如果总金额未达到输入金额则直接写入
                        xml_body = xml_body + self.__generate_dish(item, item_price)
                    else:
                        # 如果总金额超出输入金额则最后一道菜按（输入金额-总计）算
                        if self._meal_account - dish_sum + item_price > 50:
                            xml_body = xml_body + self.__generate_dish(item, self._meal_account - dish_sum + item_price)
                        else:
                            # 如果最后一道菜价小于50则菜名改为"小碟"
                            item_last = '小碟'
                            xml_body = xml_body + self.__generate_dish(item_last,self._meal_account - dish_sum + item_price)

        xml_tmp = xml_tmp + xml_body
        xml_tmp = xml_tmp + "</dish_menu>"
        return xml_tmp

    def write_xml(self, xml_str,xml_filename):
        with open(xml_filename, 'w',encoding='utf-8') as fo:
            fo.write(xml_str)


if __name__ == "__main__":
    test = create_xml('**酒店', "20180310 ", 1000, '晚餐')
    xml = test.create('dish_menu.txt')
    print(xml)
    test.write_xml(xml,'dish.xml')
