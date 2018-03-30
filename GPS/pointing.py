import math
from math import radians, degrees, sin, cos, atan2, tan

#class to implement pointing from one gps location to another
class pointing():

    def __init__(self):
        #initialize location variables
        self.ground_lat = 0.0
        self.ground_lon= 0.0
        self.ground_alt = 0.0
        self.payload_lat = 0.0
        self.payload_lon= 0.0
        self.payload_alt = 0.0
        self.distance = 0.0
        self.azimuth = 0.0
        self.elevation = 0.0

    #method to set the ground location by user input
    def setGroundLocation(self):
        print("Enter your gps location:\n")
        self.ground_lat = float(input("Latitude: "))
        self.ground_lon= float(input("Longitude: "))
        self.ground_alt = float(input("Altitude: "))

    #method to set the payload location programatically
    def setPayloadLocation(self, lat, long, alt):
        self.payload_lat = float(lat)
        self.payload_lon= float(long)
        self.payload_alt = float(alt)

    #calculates distance over a sphere, between two points
    def distanceMetersCalc(self):
        # haversine formula, see: http://www.movable-type.co.uk/scripts/latlong.html
        try:
            R = 6371000	                                            # radius of earth in meters
            dLat = math.radians(self.payload_lat-self.ground_lat)	# delta latitude in radians
            dLon = math.radians(self.payload_lon-self.ground_lon)	# delta longitude in radians
            a = math.sin(dLat/2)*math.sin(dLat/2)+math.cos(math.radians(self.ground_lat))*math.cos(math.radians(self.payload_lat))*math.sin(dLon/2)*math.sin(dLon/2)
            c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))
            d = R*c
            self.distance = d
            # self.distance = d*3280.839895 # multiply distance in Km by 3280 for feet
        except (ValueError, TypeError) as e:
            print("Get Distance Error: ", e)
            return 0

    #Returns degrees from true North, to payload
    def azimuthDegreesCalc(self):
        try:
            dLat = math.radians(self.payload_lat-self.ground_lat)		# delta latitude in radians
            dLon = math.radians(self.payload_lon-self.ground_lon)		# delta longitude in radians

            y = math.sin(dLon)*math.cos(math.radians(self.payload_lat))
            x = math.cos(math.radians(self.ground_lat))*math.sin(math.radians(self.payload_lat))-math.sin(math.radians(self.ground_lat))*math.cos(math.radians(self.payload_lat))*math.cos(dLat)
            tempBearing = math.degrees(math.atan2(y,x))		# returns the bearing from true north
            tempBearing = tempBearing % 360		#keeps it within 0-360
            self.azimuth = float(tempBearing)
        except ValueError as e:
            print ("Get Azimuth Error: ", e)
            return 0

    # Returns degrees from perpendicular to Earth surface, to payload
    def elevationDegreesCalc(self):
        try:
            deltaAlt = self.payload_alt - self.ground_alt    #delta altitude in meters
            self.elevation = float(math.degrees(math.atan2(deltaAlt, self.distance)) * -1)
        except (ValueError, TypeError) as e:
            print("Get Elevation Error: ", e)
            return 0
