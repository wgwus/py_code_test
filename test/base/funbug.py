end = 100

def compute():
    
    result = 0
    start_num = 1
    while start_num <= end:
        result += start_num
        start_num += 1
    print(result)

if __name__ == '__main__':
    compute()