class private_test:
    __private_name = 'shiyan'  #私有的属性,只在类里调用,不被外面访问
    
    def __get_private_name(self):
        return self.__private_name

#s = private_test()
#print(s.__private_name)

#https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p05_encapsulating_names_in_class.html?highlight=%E7%A7%81%E6%9C%89%E5%B1%9E%E6%80%A7



# 类属性方法

class Animal(object):
    ower = 'wanglong'
    def __init__(self,name):
        self._name = name

class Cat(Animal):

    def print1():
        print ('mimi')
print(Animal.ower)#类属性方法可以直接访问

print(Cat.ower)#继承也似可以访问
a = Animal('dob')
print (a.ower)