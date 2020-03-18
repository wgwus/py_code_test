import time
from multiprocessing import Process

def io_task():
    # time.sleep 强行挂起当前进程 1 秒钟
    # 所谓”挂起“，就是进程停滞，后续代码无法运行，CPU 无法进行工作的状态
    # 相当于进行了一个耗时 1 秒钟的 IO 操作
    # 上文提到过的，IO 操作可能会比较耗时，但它不会占用 CPU
    time.sleep(1)

def main():
    start_time = time.time()
    process_list=[]
    for i in range(5):
        process_list.append(Process(target=io_task))  # 加入到任务列表,到时候去执行
    
    for process in process_list:  #开始执行列表里的函数 
        process.start()
    for process in process_list:
        process.join()
    # 循环 IO 操作 5 次
    end_time = time.time()
    # 打印运行耗时，保留 2 位小数
    print('程序运行耗时：{:.2f}s'.format(end_time-start_time))

if __name__ == '__main__':
    main()