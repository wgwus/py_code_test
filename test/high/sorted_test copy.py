
# 元祖排序的key 没太懂
pp = [('Leborn James', 98), ('Kevin Durant', 97), ('James Harden', 96), ('Stephen Curry', 95), ('Anthony Davis', 94)]

#print(sorted(pp,key=lambda x: x[1] ,reverse=False)) #这里不懂lambda






def a(i):
    if i[1] >=96:   # 只要上手没准就能编出来结果
        return True
    else:
        return False
print(list(filter(a,pp)))



list1 = [('Shi',100), ('Yan', 75), ('Lou', 200), ('Plus', 80)]

sortedlist = sorted(list1, key=(lambda x=1: , y[x] [y for y in list1]))


print (sortedlist)