def char_count(str_):
    char_list = set(str_) #去重
    for char in char_list:
        print(char, str_.count(char)) #查询  去重了的列表逐个对比计算在此列表里的数量  

if __name__ == '__main__':

    s = input("Enter a string: ")

    char_count(s)