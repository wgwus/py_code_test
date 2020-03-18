class NewUser:
    grouop = 'shiyanlo-plus'
    # 之前题目中已经完成，不需修改

# TODO：向 NewUser 中添加方法和变量
    def __init__(self,name):
        self.name = 'name'

    @classmethod     #类的方法,可以访问类的属性 group
    def get_group(cls):
        return cls.grouop 
    @staticmethod    # 类的静态方法,可以被直接访问
    def format_userdata(id,name):
        return (name+'s id:'+str(id))


if __name__ == '__main__':
    print(NewUser.get_group())
    print(NewUser.format_userdata(109,'Lucy'))