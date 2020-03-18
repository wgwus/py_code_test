def compute(base, value):
   base =  sum(base)# 之前的代码修改后,之前的代码用的是 lis.append 会改变单独定义的[]
   print (base+value)
    

if __name__ == '__main__':
    testlist = [10, 20, 30]
    compute(testlist, 15)
    compute(testlist, 25)
    compute(testlist, 35)