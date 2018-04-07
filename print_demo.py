import linecache
#linecache只能读取UTF-8文件
import random
import re
import time
import win32api
import win32print


#生成菜价
def generate_item_price(item):
    if re.search('[\u867E\u87F9\u9C7F\u6591\u9E3D]',item) != None: #虾蟹鱿石斑鸽
        item_price = random.randrange(100, 200)
    elif re.search('[\u9E21\u725B\u9C7C\u6392\u7B19\u868C\u84B8\u7F8A\u9E2D]',item) != None:  #鱼鸡牛排骨笙蚌蒸羊鸭
        item_price = random.randrange(50, 80)
    elif re.search('[\u53C2]', item) != None:   #参
        item_price = random.randrange(150, 250)
    else:
        item_price = random.randrange(30, 50)
    return item_price;

#按格式对齐写入
def write_file(filename_tmp,item_tmp,item_price_tmp):
    open(filename_tmp, 'a+').write(item_tmp.ljust(10) + '\000' * (10 - len(item_tmp))
                               + '1      '
                               +'%s.00' % str(item_price_tmp) + '\000'*(8-len(str(item_price_tmp)))
                               + '%s.00' % str(item_price_tmp) + '\n')
    return

hotelname=input("请输入酒店名：")
while re.match(r'\w+',hotelname) == None:
    hotelname=input("请输入正确的酒店名：")

print_date=input('请输入打印时间（如20171201)：')
while re.match(r'^201[\d](0[\d]|1[0-2])(0[\d]|1[\d]|2[\d]|3[0-1])$',print_date) == None:
    print_date=input('请输入正确的打印时间（如20171201)：')

people=input('请输入人数：')
while re.match(r'[\d]+',people) == None:
    people = input('请输入正确的人数：')

sum_input=input('请输入用餐金额：')
while re.match(r'[\d]+',sum_input) == None:
    sum_input = input('请输入正确的金额：')

account=int(sum_input)
filename='1.txt'
if account<=500:
    open(filename,'w+').write("餐别：午餐  酒店名称："+hotelname+'  人数：'+people+'\n')
else:
    open(filename, 'w+').write("餐别：晚餐  酒店名称：" + hotelname + '  人数：' + people + '\n')
open(filename,"a+").write('打印时间：'+print_date[0:4]+'-'+print_date[4:6]+'-'+print_date[6:8]+' '+time.strftime("%H:%M:%S", time.localtime())+'\n')
open(filename,'a+').write('''--------------------------------------------
消费清单           数量     单价      金额  
--------------------------------------------\n
''')
item_list=[]
dish_sum=0

while dish_sum<account:#未达到总金额一直循环
        lines=len(open(filename).readlines())
        a = random.randrange(1,lines)#随机盘菜
        #从文件中对读取第a行的菜名
        theline = linecache.getline('dish_menu.txt', a)
        #匹配中文菜名
        dish_item=re.search("[\u4e00-\u9fa5]+",theline)
        #如果匹配成功则写入
        if dish_item != None:
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
win32api.ShellExecute(0,"print",filename,'/d:"%s"' %win32print.GetDefaultPrinter(),".",0)