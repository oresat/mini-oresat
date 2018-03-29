from client_socket import *
import time

#create client socket thread
socketThread = Client_Socket()

#start client thread
socketThread.start()

while True:
    #print data from server
    print(socketThread.gps_data)
    #wait 5 seconds
    time.sleep(5)
