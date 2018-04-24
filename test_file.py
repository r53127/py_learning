import json
import re
import os

hotelname = input("请输入酒店名：")
while not re.match(r'\w+', hotelname):
    hotelname = input("请输入正确的酒店名：")

json_filename='hotel_info.json'
f=open(json_filename,'r')
hotel_info=json.load(f)
for x in hotel_info:
    y=x['hotel_name']
    print(x)
    print(y)
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