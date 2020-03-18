'''

class Animal:
    def __init__(self):
        self.name ='dog'

    def __repr__(self):
        return 'Animal:{}'.format(self.name) 
animals1 = ['laofu']

an = Animal()
print (an.name)
'''
class Animal(object):
    def __init__(self,name):
        self._name = name

    def get_name(self):
        return self._name

#    def set_name(self,value):
    #    self._name=value
    
    def make_sound(self):
        print (self.get_name()+'is wawaw')
        print ('1')


class Dog(Animal):   # 继承于父类 Animal
    def make_sound(self):  # 重写父类的 make_sound 方法 重写之后实现了调用不同则显示不同的结果
        print(self.get_name() + ' is making sound wang wang wang...')


class Cat(Animal):   # 继承于父类 Animal
    def make_sound(self):  # 重写父类的 make_sound 方法
        print(self.get_name() + ' is making sound miu miu miu...')
if __name__ == "__main__":
    dog = Dog('wc')
    cat = Cat('cat')
    dog.make_sound()
    cat.make_sound()