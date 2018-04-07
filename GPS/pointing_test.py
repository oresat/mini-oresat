from pointing import *

#create pointing object
tracker = pointing()

#set payload gps location
tracker.setPayloadLocation(44.596812, -123.113287, 64)

#set ground station gps location by user input
tracker.setGroundLocation()

#calculate the pointing
tracker.calculatePointing()
#calculate distance

#print calculated variables
print("Distance: ", tracker.distance, "\nAzimuth: ", tracker.azimuth, "\nElevation: ", tracker.elevation)
