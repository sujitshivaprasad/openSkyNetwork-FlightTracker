# OpenSky API
from opensky_api import OpenSkyApi
import sys


class flights():
	
	def __init__(self):
		self.altitude, self.callsign, self.heading, self.icao24 = [], [], [], []
		self.latitude, self.longitude, self.on_ground, self.origin_country = [], [], [], []
		self.sensors, self.time_position, self.time_velocity, self.velocity, self.vertical_rate = [], [], [], [], []
		#for s in states.states:
		    #print("(%s, %s, %s, %s)" % (s.longitude, s.latitude, s.altitude, s.velocity))
		    #self.altitude = s.altitude
	def getData(self):
		api = OpenSkyApi()
		states = api.get_states()
		for s in states.states:
			self.altitude.append(s.altitude)
			self.callsign.append(s.callsign)
			self.heading.append(s.heading)
			self.icao24.append(s.icao24)
			self.latitude.append(s.latitude)
			self.longitude.append(s.longitude)
			self.on_ground.append(s.on_ground)
			self.origin_country.append(s.origin_country)
			self.sensors.append(s.sensors)
			self.time_position.append(s.time_position)
			self.time_velocity.append(s.time_velocity)
			self.velocity.append(s.velocity)
			self.vertical_rate.append(s.vertical_rate)

	def locSearch(self, loc):
		for index, country in enumerate(self.origin_country):
			if loc == country:
				if len(self.callsign[index]) > 0:
					print self.callsign[index]
				if self.altitude[index]:
					print self.altitude[index]
				if self.heading[index]:
					print self.heading[index]										



if __name__ == "__main__":
	loc = sys.argv[1]
	myFlight = flights()
	myFlight.getData()
	myFlight.locSearch(loc)


