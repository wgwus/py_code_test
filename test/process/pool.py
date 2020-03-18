

import os, time, random
from multiprocessing import Pool

# 该函数将运行在子进程中
def task(name):
    # 打印进程 ID
    print('任务{}启动运行, 进程ID：{}'.format(name, os.getpid()))
    start = time.time()
    # 假设这里有一个比较耗时的 IO 操作
    # random.random() 的值是一个 0 到 1 区间内的随机小数
    time.sleep(random.random() * 3)
    end = time.time()
    print('任务{}结束运行，耗时：{:.2f}s'.format(name, (end-start)))

if __name__=='__main__':
    print('当前为主进程，进程ID：{}'.format(os.getpid()))
    print('-----------------------------------')
    # 创建进程池，池子里面有 4 个进程可用
    p = Pool(4)
    # 将 5 个任务加入到进程池
    for i in range(1, 6):
        # apply_async 方法异步启动进程池
        # 即池子内的进程是随机接收任务的，直到所有任务完成
        p.apply_async(task, args=(i,))
    # close 方法关闭进程池
    p.close()
    # join 方法挂起主进程，直到进程池内任务全部完成
    print('开始运行子进程...')
    p.join()
    print('-----------------------------------')
    print('所有子进程运行完毕，当前为主进程，进程ID：{}'.format(os.getpid()))