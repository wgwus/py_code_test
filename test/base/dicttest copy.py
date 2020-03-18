import sys


def proce1(arg):
    b = arg.split(':')
    return f.setdefault(b[0],b[1])# setdefault 添加到字典里

def keyvalue_print(key,value):
    a =  ('id:'+key,'name:'+value)
    print (a)


if __name__ == '__main__':
    

    f={}
    for arg in sys.argv[1:]:
        proce1(arg)
    for key,value in f.items():
        keyvalue_print(key,value)


