from multiprocessing import Process, Pipe

conn1, conn2 = Pipe()# 变量内存互通

def send():
    data = 'hello shiyanlou'
    conn1.send(data)
    print('Send Data：{}'.format(data))

def recv():
    data = conn2.recv()
    print('Receive Data：{}'.format(data))

def main():
    Process(target=send).start()
    Process(target=recv).start()
    print('ok')
if __name__ == '__main__':
    main()