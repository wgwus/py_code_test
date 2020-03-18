def foo():
    print('string...')
    while True:
        res = yield 4
        print('res:',res)

g = foo()
print (next(g))
print('*'*20)
print(g.send(7))    #send 内置next  yield的值是7 然后打印 因为是next 当然从yield处执行
                # 这里send 是个赋值的操作  之前都没有赋值成功

print (next(g))
print (next(g))