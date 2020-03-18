
import time

with open('d:/1.txt','a') as f:
    count = 0
    print(type(f))
    print(f)
#    a = f.readlines()
#    print(a)
    f.write('whats ,up\n')

with open('d:/1.txt','r') as f:
    for linex in f:
        time.sleep(0.02)
        count += 1
        print (linex,end='')
    print ('Lines:',count)

