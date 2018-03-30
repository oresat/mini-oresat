from pointing import *

#create pointing object
tracker = pointing()

#set payload gps location
tracker.setPayloadLocation(44.584649, -123.115166, 53.0)

#set ground station gps location by user input
tracker.setGroundLocation()

#calculate distance
tracker.distanceMetersCalc()
#calculate azimuth in degrees
tracker.azimuthDegreesCalc()
#calculate elevation in degrees
tracker.elevationDegreesCalc()

#print calculated variables
print("Distance: ", tracker.distance, "\nAzimuth: ", tracker.azimuth, "\nElevation: ", tracker.elevation)
