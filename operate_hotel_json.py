# coding=UTF-8
import json
import os


class hotel_json():
    def __init__(self):
        self.__json_filename = 'hotel_info.json'
        if not os.path.exists(self.__json_filename):
            fo = open(self.__json_filename, 'w+', encoding='utf-8')
            fo.close()

    def check_hotel_data(self, hotel_name):
        fo = open(self.__json_filename, 'r', encoding='utf-8')
        if fo.read() == '':
            fo.close()
            return False
        else:
            fo.close()  # 需要关闭重新打开，因为文件指针已经指到结尾
            fo = open(self.__json_filename, 'r', encoding='utf-8')
            hotel_info = json.load(fo)
            for x in hotel_info:
                y = x['hotel_name']
                if y.find(hotel_name) != -1:
                    return x['hotel_name'], x['hotel_address'], x['hotel_phone']
                else:
                    continue
            return False

    def append_hotel_data(self, hotel_name, hotel_address, hotel_phone):
        hotel_tmp = []
        hotel_data = {r'hotel_name': hotel_name, r'hotel_address': hotel_address, r"hotel_phone": hotel_phone}
        fo = open(self.__json_filename, 'r', encoding='utf-8')
        if fo.read() == '':
            hotel_tmp.append(hotel_data)
            fo.close()
        else:
            fo.close()  # 文件一定要先关闭，因为if判断的时候文件指针已指到最后
            fo = open(self.__json_filename, 'r', encoding='utf-8')
            hotel_tmp = json.load(fo)
            hotel_tmp.append(hotel_data)
            fo.close()
        with open(self.__json_filename, 'w', encoding='utf-8') as fo:
            json.dump(hotel_tmp, fo, ensure_ascii=False)


if __name__ == "__main__":
    test = hotel_json()
    checkdata = test.check_hotel_data(u'荣誉大酒楼')
    if checkdata:
        print('酒店存在！', checkdata)
    else:
        test.append_hotel_data('荣誉大酒楼', "西二环中路", "88887777")
        fo = open('hotel_info.json', 'r', encoding='utf-8')
        hotel_tmp = json.load(fo)
        print(hotel_tmp)
        fo.close()
