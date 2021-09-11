import socket

target = input("Enter The Target IP : ")

port = int(input("Enter The Port For Scan It : "))

def portScan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target,port))
        return True
    except:
        return False




if portScan(port):
    print("{} is open".format(port))
else:
    print("{} is closed".format(port))