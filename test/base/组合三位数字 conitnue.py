'''
    1234 组成 互不相同 无重复的数字
'''

a = 1
b = 2
c = 3
d = 4
l = [a,b,c,d]

print (l)

for i1 in l :
    one1 = i1*100

    for i2 in l :
       # if i2 != i1:
        two2 = i2*10

        for i3 in l: 
            if ((i1 == i2) and (i1 == i3) and (i2 == i3)):
                continue

            three3=one1+two2+i3*1
            print (three3)