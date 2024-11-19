import socket
import threading 
import time
max_tr=50

#insert your ip here
ip='127.0.0.1'
#scan open tcp port
def port_checking(ipv4:str ,port:int):
    with open('check.txt','a') as file:
        socket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.settimeout(0.5)
        response =socket.connect_ex((ipv4,port))
        if  response == 0:
            file.write(ip+':'+str(port)+'\n')
            file.close()
    socket.close()
#use threading for highspeed and high performance==>export test===>2===>3===>4===>5
for port in range(1,10000):
    threading.Thread(target=port_checking,args=(ip,port)).start()
    while threading.active_count() >max_tr:
        time.sleep(0.1)
