def connect(ipaddress, ports):
    print("IP: ", ipaddress)
    print("Ports: ", ports)
    # 此处实际是创建了一个新的局部变量，并不是修改了 ipaddress 的值
    ipaddress = '10.10.10.1'
    # 修改 ports 列表的值，使用 append 向列表中增加一个元素，会影响到传入的列表 ports 的值
    ports.append(8080) #可变的数据类型会影响到调用后的数据结果

if __name__=="__main__":
    ipaddress = '192.168.1.1'
    ports = [22,23,24]
    print("Before connect:")
    print("IP: ", ipaddress)
    print("Ports: ", ports)
    print("In connect:")
    connect(ipaddress, ports)
    print("After connect:")
    print("IP: ", ipaddress)
    print("Ports: ", ports)