import sys

args1 = sys.argv[1:]
print ("arg= ")
print (args1)


a =['100:shiyan', '101:louplus', '102:jack', '103:lee']
print (a)

f={}
print(f)

for i in args1:
    b = i.split(':')
    print(b)
    f.setdefault(b[0],b[1])
print (f)

#print1 = f.items()
#print (print1)
for key,value in f.items():   # items 变量可以迭代 否则不可以
    print ('id:'+key,'name:'+value)

if __name__ == '__man__':

    for arg in sys.argv[1:]:
        proce1(arg)