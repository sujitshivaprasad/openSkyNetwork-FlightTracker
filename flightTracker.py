# OpenSky API
from opensky_api import OpenSkyApi
import sys
import collections as c
import argparse


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
			self.origin_country.append(str(s.origin_country))
			self.sensors.append(s.sensors)
			self.time_position.append(s.time_position)
			self.time_velocity.append(s.time_velocity)
			self.velocity.append(s.velocity)
			self.vertical_rate.append(s.vertical_rate)


	def requestCountry(self):
		countries = c.Counter(self.origin_country)
		print 'Aircraft origin countries found:'
		for elem in sorted(countries):
			print elem
		print '----------------------------'


	def locSearch(self, loc):
		for index, country in enumerate(self.origin_country):
			if loc == country:
				if len(self.callsign[index]) > 0:
					print 'Aircraft callsign: '+ self.callsign[index]
				if self.altitude[index]:
					print 'Altitude: ' + str(self.altitude[index])
				if self.heading[index]:
					print 'Heading: ' + str(self.heading[index])
				if self.icao24[index]:
					print 'ICAO24 address of the transmitter: ' + str(self.icao24[index])
				if self.latitude[index]:
					print 'Latitude: ' + str(self.latitude[index])
				if self.longitude[index]:
					print 'Longitude: ' + str(self.longitude[index])
				if self.on_ground[index]:
					print 'Is the aircraft currently on the ground: ' + str(self.on_ground[index])
				if self.sensors[index]:
					print 'Sensors that received messages: ' + str(self.sensors[index])
				if self.time_position[index]:
					print 'Seconds since epoch of last position report: ' + str(self.time_position[index])
				if self.time_velocity[index]:
					print 'Seconds since epoch of last velocity report: ' + str(self.time_velocity[index])
				if self.velocity[index]:
					print 'Velocity over ground in m/s: ' + str(self.velocity[index])
				if self.vertical_rate[index]:
					print 'Vertical Rate in m/s, incline is positive, decline negative: ' + str(self.vertical_rate[index])
				print '----------------------------'



if __name__ == "__main__":
	ap = argparse.ArgumentParser(description ='Learn about the aircraft flying above you')
	ap.add_argument('-c', help="origin country")
	if len(sys.argv) > 1:
		opts = vars(ap.parse_args())
		country = opts.values()
		loc = ' '.join(country)

		myFlight = flights()
		myFlight.getData()
		myFlight.requestCountry()
		myFlight.locSearch(loc)
	else:
		myFlight = flights()
		myFlight.getData()
		myFlight.requestCountry()









