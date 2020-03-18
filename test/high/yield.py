def b(n):
    current = 0
    a,b = 1,1
    while current <n:
        yield a
        a,b = b,a+b
        current +=1

b1 = b(5)
'''
for i in b1:
    print (i)

'''


print (next(b1))
print (next(b1))
print (next(b1))