# coding=UTF-8
import json
import os


class hotel_json():
    def __init__(self):
        self.__json_filename = 'hotel_info.json'
        if not os.path.exists(self.__json_filename):
            fo = open(self.__json_filename, 'w+')
            fo.close()

    def check_hotel_data(self, hotel_name):
        fo = open(self.__json_filename, 'r')
        if fo.read() == '':
            fo.close()
            return False
        else:
            hotel_info = json.load(fo)
            for x in hotel_info:
                y = x['hotel_name']
                if y.find(hotel_name):
                    return x['hotel_address'], x['hotel_phone']
                else:
                    continue
            return False

    def append_hotel_data(self, hotel_name, hotel_address, hotel_phone):
        hotel_tmp = []
        hotel_data = {r'hotel_name': hotel_name, r'hotel_address': hotel_address, r"hotel_phone": hotel_phone}
        fo = open(self.__json_filename, 'r')
        if fo.read() == '':
            hotel_tmp.append(hotel_data)
            fo.close()
        else:
            fo.close()  # 文件一定要先关闭，因为if判断的时候文件指针已指到最后
            fo = open(self.__json_filename, 'r')
            hotel_tmp = json.load(fo)
            hotel_tmp.append(hotel_data)
            fo.close()
        with open(self.__json_filename, 'w') as fo:
            json.dump(hotel_tmp, fo, ensure_ascii=False)


if __name__ == "__main__":
    test = hotel_json()
    if test.check_hotel_data('荣誉大酒店'):
        print('酒店存在！')
    else:
        test.append_hotel_data('温泉大饭店', "温泉公园", "88887777")
        fo = open('hotel_info.json', 'r')
        hotel_tmp = json.load(fo)
        print(hotel_tmp)
