import datetime
import commands as cm
import time


def vuelo1(drone):
	filename = datetime.datetime.now().strftime("Vuelo_recto_%y%m%d_%H%M%S.txt")
	f = open(filename, "wb")
	f.write("Vuelo tipo vuelo1, linea recta \n")
	drone.takeoff()
	i = 0except (KeyboardInterrupt, SystemExit):
			self.drone.update(cmd = commands.movePCMDCmd(True,0,0,0,0))
			if self.falso:
				self.drone.speed = [0, 0, 0]
			self.land()
	for i in xrange(0,50):
		print i, "   ", "hover"

	print("Movimiento")
	drone.update( cmd=cm.moverACmd(1.0, 0.0, 0.0, 0.0) )    #x, y, z, azimuth
	for i in xrange(0,100):
		f.write("Tiempo    "  + str(drone.time)+ "\n")
		f.write("Posicion  " + str(drone.position) + "\n")
		f.write("Velocidad   " + str(drone.speed) + "\n")
		f.write("GPS     " + str(drone.positionGPS) + "\n")
		f.write("Altitud     " + str(drone.altitude)  + "\n")
		f.write("Actitud    " + str(drone.attitude) + "\n")
	print ("Fin de movimiento")
	
def vuelo1b(drone):
	drone.takeoff()
	time.sleep(1)
	drone.update( cmd=cm.movePCMDCmd(True, 20.0, 0.0, 0.0, 0.0) )
	try:
		time.sleep(5)
	except (KeyboardInterrupt, SystemExit):
			drone.update(cmd = cm.movePCMDCmd(True,0,0,0,0))
			drone.land()

	drone.land()



def vuelo2(drone):
	filename = datetime.datetime.now().strftime("Vuelo_recto_giro_%y%m%d_%H%M%S.txt")
	f = open(filename, "wb")
	f.write("Vuelo tipo vuelo2, linea recta + giro \n")
	drone.takeoff()
	i = 0
	for i in xrange(0,50):
		print i, "   ", "hover"

	print("Movimiento")
	drone.update( cmd=cm.moverACmd(1, 0, 1, 0.785398) )    #x, y, z, azimuth
	for i in xrange(0,100):
		f.write("Tiempo    "  + str(drone.time)+ "\n")
		f.write("Posicion  " + str(drone.position) + "\n")
		f.write("Velocidad   " + str(drone.speed) + "\n")
		f.write("GPS     " + str(drone.positionGPS) + "\n")
		f.write("Altitud     " + str(drone.altitude)  + "\n")
		f.write("Actitud    " + str(drone.attitude) + "\n")
	print ("Fin de movimiento")
	drone.land()

def vuelo3(drone):
	filename = datetime.datetime.now().strftime("Vuelo_recto_giro_recto_%y%m%d_%H%M%S.txt")
	f = open(filename, "wb")
	f.write("Vuelo tipo vuelo3, linea recta + giro + linea recta\n")
	drone.takeoff()
	i = 0
	for i in xrange(0,50):
		print i, "   ", "hover"

	print("Movimiento")
	drone.update( cmd=cm.moverACmd(1, 0, 1, 0.78539) )    #x, y, z, azimuth
	for i in xrange(0,100):
		f.write("Tiempo    "  + str(drone.time)+ "\n")
		f.write("Posicion  " + str(drone.position) + "\n")
		f.write("Velocidad   " + str(drone.speed) + "\n")
		f.write("GPS     " + str(drone.positionGPS) + "\n")
		f.write("Altitud     " + str(drone.altitude)  + "\n")
		f.write("Actitud    " + str(drone.attitude) + "\n")
	i = 0
	for i in xrange(0,50):
		print i, "   ", "hover"

	print("Movimiento")
	drone.update( cmd=cm.moverACmd(1, 0, 1, 0) )    #x, y, z, azimuth
	for i in xrange(0,100):
		f.write("Tiempo    "  + str(drone.time)+ "\n")
		f.write("Posicion  " + str(drone.position) + "\n")
		f.write("Velocidad   " + str(drone.speed) + "\n")
		f.write("GPS     " + str(drone.positionGPS) + "\n")
		f.write("Altitud     " + str(drone.altitude)  + "\n")
		f.write("Actitud    " + str(drone.attitude) + "\n")
	print ("Fin de movimiento")
	drone.land()

def vuelo4(drone):
	filename = datetime.datetime.now().strftime("Vuelo_recto_giro_recto2_%y%m%d_%H%M%S.txt")
	f = open(filename, "wb")
	f.write("Vuelo tipo vuelo4, linea recta + giro + linea recta\n")
	drone.takeoff()
	i = 0
	for i in xrange(0,50):
		print i, "   ", "hover"

	print("Movimiento")
	drone.update( cmd=cm.moverACmd(1, 0, 1, 0.78539) )    #x, y, z, azimuth
	for i in xrange(0,100):
		f.write("Tiempo    "  + str(drone.time)+ "\n")
		f.write("Posicion  " + str(drone.position) + "\n")
		f.write("Velocidad   " + str(drone.speed) + "\n")
		f.write("GPS     " + str(drone.positionGPS) + "\n")
		f.write("Altitud     " + str(drone.altitude)  + "\n")
		f.write("Actitud    " + str(drone.attitude) + "\n")
	i = 0
	for i in xrange(0,50):
		print i, "   ", "hover"

	print("Movimiento")
	drone.update( cmd=cm.moverACmd(1, 1, 1, 0.78539) )    #x, y, z, azimuth
	for i in xrange(0,100):
		f.write("Tiempo    "  + str(drone.time)+ "\n")
		f.write("Posicion  " + str(drone.position) + "\n")
		f.write("Velocidad   " + str(drone.speed) + "\n")
		f.write("GPS     " + str(drone.positionGPS) + "\n")
		f.write("Altitud     " + str(drone.altitude)  + "\n")
		f.write("Actitud    " + str(drone.attitude) + "\n")
	print ("Fin de movimiento")
	drone.land()

def vuelo5(drone):
	filename = datetime.datetime.now().strftime("Vuelo_cuadrado_%y%m%d_%H%M%S.txt")
	f = open(filename, "wb")
	f.write("Vuelo tipo vuelo5, cuadrado 1x1\n")
	drone.takeoff()
	i = 0
	for i in xrange(0,50):
		print i, "   ", "hover"

	print("Movimiento")
	drone.update( cmd=cm.moverACmd(1, 0, 1, 0) )    #x, y, z, azimuth
	for i in xrange(0,100):
		f.write("Tiempo    "  + str(drone.time)+ "\n")
		f.write("Posicion  " + str(drone.position) + "\n")
		f.write("Velocidad   " + str(drone.speed) + "\n")
		f.write("GPS     " + str(drone.positionGPS) + "\n")
		f.write("Altitud     " + str(drone.altitude)  + "\n")
		f.write("Actitud    " + str(drone.attitude) + "\n")
	i = 0
	for i in xrange(0,50):
		print i, "   ", "hover"

	print("Movimiento")
	drone.update( cmd=cm.moverACmd(1, 1, 1, 0) )    #x, y, z, azimuth
	for i in xrange(0,100):
		f.write("Tiempo    "  + str(drone.time)+ "\n")
		f.write("Posicion  " + str(drone.position) + "\n")
		f.write("Velocidad   " + str(drone.speed) + "\n")
		f.write("GPS     " + str(drone.positionGPS) + "\n")
		f.write("Altitud     " + str(drone.altitude)  + "\n")
		f.write("Actitud    " + str(drone.attitude) + "\n")

	i = 0
	for i in xrange(0,50):
		print i, "   ", "hover"

	print("Movimiento")
	drone.update( cmd=cm.moverACmd(0, 1, 1, 0) )    #x, y, z, azimuth
	for i in xrange(0,100):
		f.write("Tiempo    "  + str(drone.time)+ "\n")
		f.write("Posicion  " + str(drone.position) + "\n")
		f.write("Velocidad   " + str(drone.speed) + "\n")
		f.write("GPS     " + str(drone.positionGPS) + "\n")
		f.write("Altitud     " + str(drone.altitude)  + "\n")
		f.write("Actitud    " + str(drone.attitude) + "\n")

	i = 0
	for i in xrange(0,50):
		print i, "   ", "hover"

	print("Movimiento")
	drone.update( cmd=cm.moverACmd(0, 0, 1, 0) )    #x, y, z, azimuth
	for i in xrange(0,100):
		f.write("Tiempo    "  + str(drone.time)+ "\n")
		f.write("Posicion  " + str(drone.position) + "\n")
		f.write("Velocidad   " + str(drone.speed) + "\n")
		f.write("GPS     " + str(drone.positionGPS) + "\n")
		f.write("Altitud     " + str(drone.altitude)  + "\n")
		f.write("Actitud    " + str(drone.attitude) + "\n")
	print ("Fin de movimiento")
	drone.land()


class Dronefalso():
	def __init__(self):
		self.position=(0,0,0)
		self.speed= (0,0,0)
		self.attitude = (0,0,0)
		self.positionGPS=(0,0,0)
		self.altitude = 0
		self.flyingState=0
		self.battery = 0
		self.time = 0

	def takeoff(self):
		return
	def land(self):
		return
	def update(self, asd):
		return
	def flyToAltitude(self, h):
		return
	def requestAllStates(self):
		return
