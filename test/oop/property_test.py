class Animal:
    def __init__(self):
        self.__age = 3   # 把 age 设置为私有属性
    @property
    def age(self):    # get_age 方法获取属性值
        return self.__age
    @age.setter
    def age(self, value):     # set_age 方法修改属性值，在其中对值做判断
        if isinstance(value,int):
            self.__age = value
        else:
            raise ValueError
    @age.deleter
    def age(self):
        print('delete')
        del self.__age
cat = Animal()
cat.age = 6    #这里可以更改了类属性值 非常方便
print (cat.age)
#del cat.age # 删除之后 就不能访问类属性了
#print (cat.age)
