import win32api
import win32print
import time
import linecache
import random
import re
#linecache只能读取UTF-8文件


hotelname=input("请输入餐馆名：")
print_date=input('请输入打印时间：')
filename='1.txt'
open(filename,'w+').write("餐别：晚餐  餐馆名称："+hotelname+'\n')
open(filename,"a+").write('打印时间：'+print_date+' '+time.strftime("%H:%M:%S", time.localtime())+'\n')
open(filename,'a+').write('''-----------------------------------
消费清单   数量     单价      金额  
-----------------------------------\n
''')
item_list=[]
for i in range(1,9):#for循环几次
    a = random.randrange(1,20)#1-9中生成随机数
    #从文件中对读取第a行的数据
    theline = linecache.getline('dish_menu.txt', a)
    #匹配中文菜名
    dish_item=re.search("[\u4e00-\u9fa5]+",theline)
    #如果匹配成功则写入
    if dish_item!=None:
        item=dish_item.group()
        if item not in item_list:
            open(filename,'a+').write(item+'\n')
            item_list.append(item)
        else:
            continue
    else:
        continue