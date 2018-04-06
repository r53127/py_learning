import linecache
import random
import re
import time
import win32api
import win32print

#linecache只能读取UTF-8文件
def generate_item_price(item_number):
    if 1<=item_number<=13:
        item_price = random.randrange(50, 100)
    elif 14<=item_number<=29:
        item_price = random.randrange(30, 50)
    elif 30<=item_number<=37:
        item_price = random.randrange(150, 200)
    elif 38<=item_number<=58:
        item_price = random.randrange(50, 100)
    elif 59<=item_number<=114:
        item_price = random.randrange(70, 100)
    elif 207<=item_number<=222:
        item_price = random.randrange(70, 100)
    elif 153<=item_number<=177:
        item_price = random.randrange(50, 100)
    else:
        item_price = random.randrange(30, 50)
    return item_price;

hotelname=input("请输入餐馆名：")
print_date=input('请输入打印时间：')
people=input('请输入人数：')
sum_input=input('请输入用餐金额：')
account=int(sum_input)
filename='1.txt'
if account<=500:
    open(filename,'w+').write("餐别：午餐  餐馆名称："+hotelname+'  人数：'+people+'\n')
else:
    open(filename, 'w+').write("餐别：晚餐  餐馆名称：" + hotelname + '  人数：' + people + '\n')
open(filename,"a+").write('打印时间：'+print_date[0:4]+'-'+print_date[4:6]+'-'+print_date[6:8]+' '+time.strftime("%H:%M:%S", time.localtime())+'\n')
open(filename,'a+').write('''--------------------------------------------
消费清单           数量     单价      金额  
--------------------------------------------\n
''')
item_list=[]
dish_sum=0

while dish_sum<account:#未达到总金额一直循环
        a = random.randrange(1,246)#随机盘菜
        #从文件中对读取第a行的菜名
        theline = linecache.getline('dish_menu.txt', a)
        #匹配中文菜名
        dish_item=re.search("[\u4e00-\u9fa5]+",theline)
        #如果匹配成功则写入
        if dish_item != None:
            item=dish_item.group()
            if item not in item_list:
                item_price=generate_item_price(a)
                dish_sum = dish_sum + item_price
                if dish_sum<=account:
                    #如果总金额未达到输入金额则直接写入
                    open(filename,'a+').write(item.ljust(10)+'\000'*(10-len(item))+'1       '+'%s.00' %str(item_price)+'   '+'%s.00' %str(item_price)+'\n')
                else:
                    #如果总金额超出输入金额则按最后一道菜按（输入金额-总计）算
                    if account-dish_sum+item_price>50:
                        open(filename, 'a+').write(
                            item.ljust(10) + '\000' * (10 - len(item)) + '1       ' + '%s.00' %str(account-dish_sum+item_price) + '     ' + '%s.00' %str(
                            account-dish_sum+item_price) + '\n')
                    else:
                        #如果最后一道菜价小于50则菜名改为"小碟"
                        item_last='小碟'
                        open(filename, 'a+').write(
                            item_last.ljust(10) + '\000' * (10 - len(item_last)) + '1       ' + '%s.00' % str(
                                account - dish_sum + item_price) + '   ' + '%s.00' % str(
                                account - dish_sum + item_price) + '\n')
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
win32api.ShellExecute(0,"print",filename,'/d:"%s"' %win32print.GetDefaultPrinter(),".",0)