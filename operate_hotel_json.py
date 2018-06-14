# coding=UTF-8
import json
import os


class hotel_json():
    def __init__(self):
        self.__json_filename = 'hotel_info.json'
        if not os.path.exists(self.__json_filename):
            with open(self.__json_filename, 'w', encoding='utf-8') as fo:
                hotel_tmp = []
                json.dump(hotel_tmp, fo, ensure_ascii=False)


    def check_hotel_data(self, hotel_name):
        with open(self.__json_filename, 'r', encoding='utf-8') as fo:
            hotel_info = json.load(fo)
            for x in hotel_info:
                y = x['hotel_name']
                if y.find(hotel_name) != -1:
                    return x['hotel_name'], x['hotel_address'], x['hotel_phone']
                else:
                    continue
            else:
                return False

    def append_hotel_data(self, hotel_name, hotel_address, hotel_phone):
        hotel_data = {r'hotel_name': hotel_name, r'hotel_address': hotel_address, r"hotel_phone": hotel_phone}
        with open(self.__json_filename, 'r', encoding='utf-8') as fo:
            hotel_tmp = json.load(fo)
            hotel_tmp.append(hotel_data)
        with open(self.__json_filename, 'w', encoding='utf-8') as fo:
            json.dump(hotel_tmp, fo, ensure_ascii=False)

    def replace_hotel_data(self, hotel_name, hotel_address, hotel_phone):
        hotel_data = {r'hotel_name': hotel_name, r'hotel_address': hotel_address, r"hotel_phone": hotel_phone}
        with open(self.__json_filename, 'r', encoding='utf-8') as fo:
            hotel_info = json.load(fo)
            for index,value in enumerate(hotel_info):
                if value['hotel_name'].find(hotel_name)!=-1:
                    hotel_info[index]=hotel_data
        with open(self.__json_filename, 'w', encoding='utf-8') as fo:
            json.dump(hotel_info, fo, ensure_ascii=False)

            
    def read_data(self):
        with open(self.__json_filename, 'r', encoding='utf-8') as fo:
            hotel_info = json.load(fo)
            return hotel_info


if  __name__ == "__main__":
    test = hotel_json()
    checkdata = test.check_hotel_data('温泉酒店')
    if checkdata:
        print('酒店存在！', checkdata)
    else:
        test.append_hotel_data('温泉酒店', "****路", "88887777")
        fo = open('hotel_info.json', 'r', encoding='utf-8')
        hotel_tmp = json.load(fo)
        print(hotel_tmp)
        fo.close()
