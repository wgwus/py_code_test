import  socket
 
def port_status(ip,port):
 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
    try:
 
        server.connect((ip,port))
        print('port open')
        server.close()
 
    except Exception as err:
        print ("port closed")
 
if __name__ == "__main__":
    ip="127.0.0.1"
    port_status(ip,80)