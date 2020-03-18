class NewUser(object):
    
    def __init__(self,id,name):
      self.id = id
      self._name = name
    @property
    def name (self):
       return self._name
    
    @name.setter
    def name(self,value):
        if isinstance(value,str):
            self._name = value# 这里有点不明白
        else:
            raise ValueError
    @name.getter
    def name(self):
        return self._name



# TODO：按题目要求修改 NewUser 的定义

if __name__ == '__main__':
    user1 = NewUser(101, 'Jack')
    user1.name = 'Lou'
    user1.name = 'Jackie'
    user2 = NewUser(102, 'Louplus')
    print(user1.name)
    print(user2.name)
