import sys
import csv
'''基本使用了继承,但是对self这样的操作还是不习惯,基本都是方法调用'''
class Args1():
    
    args1 = sys.argv[1:]
    def __init__(self):
        pass

    def index1(self):
        index1 = self.args1.index('-c')
        test_cfg = self.args1[index1+1]
        return test_cfg
    #print (test_cfg)
    #ins1 = Config(test_cfg)
    #ins1.get_config()    

    def index2(self):
        index2 = self.args1.index('-d')
        user_csv = self.args1[index2+1] # 
        return user_csv
    
    def index3(self):
        index3 = self.args1.index('-o')
        gongzi_csv = self.args1[index3+1] # 
        return gongzi_csv


class Config(Args1):
    def __init__(self):
        pass
    
    def shebao(self,gongzi): #计算社保
        #print (self._open1())
        jishuL = self._open1().get('JiShuL')
        jishuH = self._open1().get('JiShuH')
        #test_pirnt = self._open1().get('JiShuL')
        #print (test_pirnt)
        if gongzi < jishuL:
            jishu  = jishuL
        elif gongzi > jishuH:
            jishu  = jishuH
        else:
            jishu = gongzi
        yanglao = jishu*self._open1().get('YangLao')
        gongjijin = jishu*self._open1().get('GongJiJin')
        jishu*self._open1().get('YangLao')
        yiliao = jishu*self._open1().get('YiLiao')
        print (yiliao)
        shiye = jishu*self._open1().get('ShiYe')
        shebao = yanglao+gongjijin+shiye+yiliao
        print (shebao)
        return shebao
    def geshui(self,ynssde):
        ynssde = ynssde-3500
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

    def _open1(self):
        dict1={}
        with open(self.index1(),'r') as f:  #self.index1 继承了 Args1类里面的-c 后面的文件
            for i in f.readlines():
                i = i.replace(' ','')# 替换掉空字符
                i = i.strip('\n') #去掉回车
                split1 = i.split('=')
                #strip1_1 = strip1[0]
                #strip1_2 = strip1[1]
                dict1.setdefault(split1[0],float(split1[1]))#float 字符串转换成数字
        #print (dict1) 
        #print (dict1.get('JiShuL'))
        return dict1

    def _open2(self):
        dict2={}
        with open(self.index2(),'r')as f:
            reader = csv.reader(f)    #csv文件读取 需要逐行放出 才能处理
            for line in reader:
                dict2.setdefault(line[0],float(line[1]))  #list 切片可以直接存入dict
        return dict2


class UserData(Config):

    def __init__(self):
        pass
    def calculator(self):
        pass
        #for key ,value in self._open2().items():
         #   id = key
          #  gongzi = value

    def dmupfile(self):
        
        with open(self.index3(), 'a') as f:
            writer = csv.writer(f)
            for key, value in self._open2().items():
                id = key
                gongzi = value
                shebao = self.shebao(gongzi)
                geshui = self.geshui(gongzi)
                shuihou = gongzi-geshui-shebao
                writer.writerow([id, gongzi, shebao, geshui, shuihou])
    

    



   
if __name__ == "__main__":
    run = UserData()
    run.dmupfile()