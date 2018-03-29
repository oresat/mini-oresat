
import socket
import time
import gpsd
import traceback

#fixed length variable
MSGLEN =4

#connect to the local gpsd
gpsd.connect()

#create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the socket
s.bind(("192.168.42.1", 1000))
#start listening
s.listen(5)

#print listening
#print("Listening for client")

#server loop
while True:
	try:
		#accept a client connection
		client, address = s.accept()
		#print the connection info
		#print("Connection from: ", address)

		#message declaration
		#baseMessage = str('This is a message! datetime: ')

		#add time to message
		#message = baseMessage + time.asctime()

		#get gps position
		packet = gpsd.get_current()

		#add gps data to message
		message = "Latitude: " + str(packet.lat) + "\nLongetude: " + str(packet.lon) + "\nAltitude: " + str(packet.alt)
		#message = str(packet)

		#message length
		length = len(message)
		messagelen = str(length).zfill(4).encode('UTF-8')
		message = message.encode('UTF-8')

		#print(messagelen)
		#print("Message: ", message)

		#sent tracker
		totalsent = 0
		#send message length loop
		while totalsent < MSGLEN:
			#send message length
			sent = client.sendto(messagelen[totalsent:], address)
			#check for broken connection
			if sent == 0:
				raise RuntimeError("socket connection broken")
			#add to totalsent
			totalsent = totalsent + sent


		#print message length success
		#print("Message length was sent successfully")


		#sent tracker
		totalsent = 0
		#send message loop
		while totalsent < length:
	        	#send message
		        sent = client.sendto(message[totalsent:], address)

	        	#check for broken connection
		        if sent == 0:
	        	    raise RuntimeError("socket connection broken")
		        #add to totalsent
	        	totalsent = totalsent + sent

		#print message success
		#print("Message was sent successfully")
		
		#close connection
		client.close()
	except:
		#if the connection is broken or there is an error
		#close the socket and continue to the next client connection
		client.close()
		traceback.print_exc()

		#continue

