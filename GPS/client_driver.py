from client_socket import *
from pointing import *
import time

#create client socket thread
socketThread = Client_Socket()

#start client thread
socketThread.start()

#create pointing object
tracker = pointing()

#ask for ground station gps location
tracker.setGroundLocation()

while True:
    #feed the payload gps data to the pointing program
    tracker.setPayloadLocation(socketThread.lat, socketThread.lon, socketThread.alt)

    #calculate pointing values
    tracker.calculatePointing()

    #print the pointing values
    print("Azimuth: ", tracker.azimuth, "\nElevation: ", tracker.elevation)

    #wait 5 seconds
    time.sleep(5)