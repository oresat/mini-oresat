
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

    #method to set the ground location by user input
    def setGroundLocation(self):
        print("Enter your gps location:\n")
        self.ground_lat = float(input("Latitude: "))
        self.ground_lon= float(input("Longitude: "))
        self.ground_alt = float(input("Altitude: "))

    #method to set the payload location programatically
    def setPayloadLocation( lat, long, alt):
        self.payload_lat = float(lat)
        self.payload_lon= float(long)
        self.payload_alt = float(alt)

    def distanceMetersCalc(self):
        ''' calculates distance over a sphere, between two points '''
		# haversine formula, see: http://www.movable-type.co.uk/scripts/latlong.html
		try:
			R = 6371000									# radius of earth in meters
			dLat = math.radians(self.payload_Lat-self.ground_lat)	# delta latitude in radians
			dLon = math.radians(self.payload_Long-self.ground_long)	# delta longitude in radians
			a = math.sin(dLat/2)*math.sin(dLat/2)+math.cos(math.radians(self.ground_Lat))*math.cos(math.radians(self.payload_lat))*math.sin(dLon/2)*math.sin(dLon/2)
			c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))
			d = R*c
			self.distance = d
			# self.distance = d*3280.839895 # multiply distance in Km by 3280 for feet
		except (ValueError, TypeError) as e:
			print("Get Distance Error: ", e)
			return 0

    def azimuthDegreesCalc(self):
        pass

    def elevationDegreesCalc(self):
        pass

    """
    def getEleDegrees(self, payloadAlt, stationAlt, distance):
		''' Returns degrees from perpendicular to Earth surface, to payload '''
		try:
			deltaAlt = payloadAlt - stationAlt
			return float(math.degrees(math.atan2(deltaAlt, distance)))
		except (ValueError, TypeError) as e:
			print("Get Elevation Error: ", e)
			return 0


	def getTargetDistance(self, trackerLat, trackerLon, remoteLat, remoteLon):
		''' Returns distance over a sphere, between two points '''
		# haversine formula, see: http://www.movable-type.co.uk/scripts/latlong.html
		try:
			R = 6371000									# radius of earth in meters
			dLat = math.radians(remoteLat-trackerLat)	# delta latitude in radians
			dLon = math.radians(remoteLon-trackerLon)	# delta longitude in radians
			a = math.sin(dLat/2)*math.sin(dLat/2)+math.cos(math.radians(trackerLat))*math.cos(math.radians(remoteLat))*math.sin(dLon/2)*math.sin(dLon/2)
			c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))
			d = R*c
			return int(d)
			# return d*3280.839895 # multiply distance in Km by 3280 for feet
		except (ValueError, TypeError) as e:
			print("Get Distance Error: ", e)
			return 0


	def getAzDegrees(self, trackerLat, trackerLon, remoteLat, remoteLon):
		''' Returns degrees from true North, to payload '''
		try:
			dLat = math.radians(remoteLat-trackerLat)		# delta latitude in radians
			dLon = math.radians(remoteLon-trackerLon)		# delta longitude in radians

			y = math.sin(dLon)*math.cos(math.radians(remoteLat))
			x = math.cos(math.radians(trackerLat))*math.sin(math.radians(remoteLat))-math.sin(math.radians(trackerLat))*math.cos(math.radians(remoteLat))*math.cos(dLat)
			tempBearing = math.degrees(math.atan2(y,x))		# returns the bearing from true north
			tempBearing = tempBearing % 360		#keeps it within 0-360
			return float(tempBearing)
		except ValueError as e:
			print ("Get Azimuth Error: ", e)
			return 0
    """
