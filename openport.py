import socket

target = input("Enter The Target IP : ")

port = int(input("Enter The Port Would you open it : "))

def openPort(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((target, port))                                                    
        sock.listen(1)
        return True
    except:
        return False
    
    
if openPort(port):
    print(f"Port {port} has been opened by success ...")
else:
    print(f"Port {port} has not been opened ...")