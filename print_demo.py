#!/usr/bin/python
# -*- coding: <encoding name> -*-
import linecache
#linecache只能读取UTF-8文件
import random
import re
import time
import win32api
import win32print
import os


#生成菜价
def generate_item_price(item):
    if re.search('[\u523A][\u8EAB]|[\u9F99][\u867E]|[\u53C2]',item) != None: #刺身|龙虾|参
        item_price = random.randrange(200, 300)
    elif re.search('[\u867E\u87F9\u9C7F\u6591\u9E3D]',item) != None: #虾蟹鱿石斑鸽
        item_price = random.randrange(150, 200)
    elif re.search('[\u9E21\u725B\u9C7C\u6392\u7B19\u868C\u84B8\u7F8A\u9E2D]',item) != None:  #鱼鸡牛排骨笙蚌蒸羊鸭
        item_price = random.randrange(100, 150)
    elif re.search('[\u87F9]|[\u5927][\u867E]',item) != None: #蟹|大虾
        item_price = random.randrange(100,200)
    elif re.search('[\u996D]',item) != None:  #饭
        item_price = random.randrange(30, 50)
    else:
        item_price = random.randrange(60, 90)
    return item_price

#按格式对齐写入
def write_file(filename_tmp,item_tmp,item_price_tmp):
    open(filename_tmp, 'a+').write(item_tmp.ljust(10) + '\000' * (10 - len(item_tmp))
                               + '1      '
                               +'%s.00' % str(item_price_tmp) + '\000'*(8-len(str(item_price_tmp)))
                               + '%s.00' % str(item_price_tmp) + '\n')
    return

def generate_time(account_tmp):
    if account_tmp<500:
        h=random.randrange(13, 15)
        m=random.randrange(0, 60)
        s=random.randrange(0, 60)
    else:
        h=random.randrange(19, 23)
        m=random.randrange(0, 60)
        s=random.randrange(0, 60)
    time_tmp=str(h).zfill(2)+':'+str(m).zfill(2)+':'+str(s).zfill(2)
    return time_tmp


dish_file='dish_menu.txt'
while not os.path.exists(dish_file):
    print("请把菜谱文件命名为dish_menu.txt并和程序放在一起再继续...")
    os.system('pause')

hotelname=input("请输入酒店名：")
while not re.match(r'\w+',hotelname):
    hotelname=input("请输入正确的酒店名：")

print_date=input('请输入打印时间（如20171201)：')
while  not re.match(r'^201[\d](0[\d]|1[0-2])(0[\d]|1[\d]|2[\d]|3[0-1])$',print_date):
    print_date=input('请输入正确的打印时间（如20171201)：')

#people=input('请输入人数：')
#while not re.match(r'[\d]+',people) :
#   people = input('请输入正确的人数：')
#
sum_input=input('请输入用餐金额：')
while not re.match(r'[\d]+',sum_input):
    sum_input = input('请输入正确的金额：')

account=int(sum_input)
filename='1.txt'


if account<=500:
    open(filename,'w+').write("餐别：午餐  酒店名称："+hotelname+'\n')
else:
    open(filename, 'w+').write("餐别：晚餐  酒店名称：" + hotelname+ '\n')
#
# open(filename,"a+").write('打印时间：'+print_date[0:4]+'-'+print_date[4:6]+'-'+print_date[6:8]+' '+time.strftime("%H:%M:%S", time.localtime())+'\n')
open(filename,"a+").write('打印时间：'+print_date[0:4]+'-'+print_date[4:6]+'-'+print_date[6:8]+' '+generate_time(account)+'\n')
open(filename,'a+').write('''--------------------------------------------
消费清单           数量     单价      金额  
--------------------------------------------\n
''')
item_list=[]
dish_sum=0
lines = len(open(dish_file,encoding='UTF-8').readlines())

while dish_sum<account:#未达到总金额一直循环
        a = random.randrange(1,lines)#随机盘菜
        #从文件中对读取第a行的菜名
        theline = linecache.getline(dish_file, a)
        #匹配中文菜名
        dish_item=re.search("[\u4e00-\u9fa5]+",theline)
        #如果匹配成功则写入
        if dish_item:
            item=dish_item.group()
            if item not in item_list:
                item_price=generate_item_price(item)
                dish_sum = dish_sum + item_price
                if dish_sum<=account:
                    #如果总金额未达到输入金额则直接写入
                    write_file(filename,item, item_price)
                    #open(filename,'a+').write(item.ljust(10)+'\000'*(10-len(item))+'1       '+'%s.00' %str(item_price)+'   '+'%s.00' %str(item_price)+'\n')
                else:
                    #如果总金额超出输入金额则最后一道菜按（输入金额-总计）算
                    if account-dish_sum+item_price>50:
                        write_file(filename, item, account-dish_sum+item_price)
                        #open(filename, 'a+').write(item.ljust(10) + '\000' * (10 - len(item)) + '1       ' + '%s.00' %str(account-dish_sum+item_price) + '     ' + '%s.00' %str(account-dish_sum+item_price) + '\n')
                    else:
                        #如果最后一道菜价小于50则菜名改为"小碟"
                        item_last='小碟'
                        write_file(filename, item_last, account - dish_sum + item_price)
                        #open(filename, 'a+').write(item_last.ljust(10) + '\000' * (10 - len(item_last)) + '1       ' + '%s.00' % str(account - dish_sum + item_price) + '   ' + '%s.00' % str(account - dish_sum + item_price) + '\n')
                item_list.append(item)
            else:
                continue
        else:
            continue

open(filename, 'a+').write('''
--------------------------------------------
优惠金额：0.00元
应付金额：''')
open(filename,'a+').write(str(account)+'''元
--------------------------------------------
    ''')
#win32api.ShellExecute(0,"print",filename,'/d:"%s"' %win32print.GetDefaultPrinter(),".",0)