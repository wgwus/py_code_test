import sys



def a(lv_list_5x1j,money):
    lvsum = 0
    for i in lv_list_5x1j:
       a = (i*money)
       lvsum +=a
        
       # behand5x1j.append(i*money) 之前用appen sum 来计算也是可以的 又省略了判断
   # lvsum=sum(behand5x1j)

    return lvsum  # 返回一个值但是又不影响其他值得改变 ,当调用的时候生成了值移作他用



print(a)

def shud_shui(ynssde):
    if ynssde <=0:   #当工资小于3500 的时候 不争税  所以应缴纳的税额是0
        shud_shui1=0
    elif 0< ynssde <=1500:
        shud_shui1=ynssde*0.03-0
    elif 1500 <ynssde<=4500:
        shud_shui1=ynssde*0.1-105
    elif 4500 <ynssde<=9000:
        shud_shui1=ynssde*0.2-555
    elif 9000 <ynssde<=35000:
        shud_shui1=ynssde*0.25-1005
    elif 35000 <ynssde<=55000:
        shud_shui1=ynssde*0.3-2755
    elif 55000 <ynssde<=80000:
        shud_shui1=ynssde*0.35-5505
    else:
        shud_shui1=ynssde*0.45-13505
    
    return shud_shui1
def arg_f(arg1):
    for i in arg1:
        print (i)
        i =  i.split(':')
        #number1 = i[0]
        #money = int(i[1])
        list1.append(i)
    return list1
if __name__ == "__main__":
    lv_list_5x1j = [0.08,0.06,0.005,0.02]
    behand5x1j=[]  # 五险一金之后
    list1 = []
    arg1 = sys.argv[1:]
    
    i = arg_f(arg1)
    arg_iter = iter(i)
    while 1:

        i = next(arg_iter)
        number1  = i[0]
        money = float(i[1])

        wx1j_after = a(lv_list_5x1j,money)###调用五险一金

        ynssde = money - wx1j_after -3500 #应纳税所得额


        b = shud_shui(ynssde)
        moneybehand = money-wx1j_after-b

        print(i[0]+':'+'%.2f' % moneybehand)