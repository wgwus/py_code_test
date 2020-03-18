import sys

def copy_file(src,dst):
    with open(src,'r') as src_file:
        with open(dst,'w') as dst_file:
            for i in src_file.readlines():
                dst_file.write(i)



if __name__ == '__main__':
    one1txt = ('d:/1.txt')
    other_txt = ('d:/2.txt')
    copy_file(one1txt,other_txt)
    with open (other_txt,'r')as f:
        print(f.read())