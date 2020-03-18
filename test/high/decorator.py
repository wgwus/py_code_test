from datetime import datetime

def log(func):
    def decorator(*args,**kwargs):
        print("function "+func.__name__+'has beencalld at'+ datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return func(*args,**kwargs)
    return decorator

@log
def add(x,y):
    return x+y
#add = log(add)
add(1,2)