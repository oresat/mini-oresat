import socket
from threading import Thread
import time

class Client_Socket(Thread):

    def __init__(self):
        Thread.__init__(self)
        #message length
        self.MSGLEN = 4
        #gps data holder
        self.gps_data = ''
        #connected flag
        self.connected = False
        #socket variable
        self.sock = None

    def __del__(self):
        #close the socket
        self.sock.close()

    def connect(self, host, port):
        if self.connected == False:
            #create socket
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #connect to gps_server
            self.sock.connect((host, port))
            self.connected = True

    def recieve(self):
        #message length holder
        lenchunks = []
        #recieved tracker
        bytes_recd = 0
        #recieve message length loop
        while bytes_recd < self.MSGLEN:
            #recieve the rest of the message length unless it is larger then 2048
            chunk = self.sock.recv(min(self.MSGLEN - bytes_recd, 2048))
            #check for broken connection
            if chunk == b'':
                self.connected = False
                self.sock.close()
                print("Broken Connection")
                return ''
            #add message length part to message holder
            lenchunks.append(chunk)
            #add to recieved tracker
            bytes_recd = bytes_recd + len(chunk)

        #convert value to int
        length = int(b''.join(lenchunks).decode())
        #print(length)

        #message holder
        chunks = []
        #recieved tracker
        bytes_recd = 0
        #recieve message loop
        while bytes_recd < length:
            #recieve the rest of the message unless it is larger then 2048
            chunk = self.sock.recv(min(length - bytes_recd, 2048))
            #check for broken connection
            if chunk == b'':
                self.connected = False
                self.sock.close()
                print("Broken connection")
                return ''
            #add message part to message holder
            chunks.append(chunk)
            #add to recieved tracker
            bytes_recd = bytes_recd + len(chunk)

        self.connected = False
        #return message
        return b''.join(chunks).decode()

    def run(self):
        #time holder
        lastChecked = 0
        #loop to retrieve data every 5 seconds
        while True:
                #check every 5 seconds
                if (time.time() - lastChecked) > 5 and self.connected == False:
                    #set lastChecked
                    lastChecked = time.time()
                    #connect to server
                    self.connect("192.168.42.1", 1000)
                    #obtain gps_data
                    self.gps_data = self.recieve()
                    #close socket
                    self.sock.close()
