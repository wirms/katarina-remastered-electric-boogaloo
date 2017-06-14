def prueba5(drone):
	
	f = open("Datos_vuelo_prueba5.txt", "wb")
	f.write("Test de despegue y aterrizaje   \n")
	drone.takeoff()
	print("")
	print("")
	print("")
	print("")
	print("Estado del drone")
	print("")
	i= 0
	for i in range(0,500):
		print "Posicion  ",   drone.position
		print "Velocidad   ", drone.speed
		print "GPS    ",   drone.positionGPS
		print "Altitud   ", drone.altitude
		print "Estado    ",   drone.flyingState, "    Bateria   ", drone.battery
		f.write(str(i) + "\n")
		f.write("Posicion  " + str(drone.position) + "\n")
		f.write("Velocidad   " + str(drone.speed) + "\n")
		f.write("GPS     " + str(drone.positionGPS) + "\n")
		f.write("Altitud     " + str(drone.altitude)  + "\n")
		f.write("Estado   " + str(drone.flyingState) + "\n")
		f.write("\n")
		f.write("\n")

	print ("Fin de vuelo")
	drone.land()

def prueba6(drone):
	
	f = open("Datos_vuelo_prueba6.txt", "wb")
	f.write("Test de despegue y cambio de altura   \n")
	drone.takeoff()
	print("")
	print("")
	print("")
	print("")
	print("Estado del drone")
	print("")
	i= 0
	for i in range(0,100):
		print "Posicion  ",   drone.position
		print "Velocidad   ", drone.speed
		print "GPS    ",   drone.positionGPS
		print "Altitud   ", drone.altitude
		print "Estado    ",   drone.flyingState, "    Bateria   ", drone.battery
		f.write(str(i) + str(drone.time) + "\n")
		f.write("Posicion  " + str(drone.position) + "\n")
		f.write("Velocidad   " + str(drone.speed) + "\n")
		f.write("GPS     " + str(drone.positionGPS) + "\n")
		f.write("Altitud     " + str(drone.altitude)  + "\n")
		f.write("Estado   " + str(drone.flyingState) + "\n")
		f.write("\n")
		f.write("\n")

	f.write("Cambio de altitud  \n")
	drone.flyToAltitude(2)
	i= 0
	for i in range(0,100):
		print "Posicion  ",   drone.position
		print "Velocidad   ", drone.speed
		print "GPS    ",   drone.positionGPS
		print "Altitud   ", drone.altitude
		print "Estado    ",   drone.flyingState, "    Bateria   ", drone.battery
		f.write(str(i) + str(drone.time) + "\n")
		f.write("Posicion  " + str(drone.position) + "\n")
		f.write("Velocidad   " + str(drone.speed) + "\n")
		f.write("GPS     " + str(drone.positionGPS) + "\n")
		f.write("Altitud     " + str(drone.altitude)  + "\n")
		f.write("Estado   " + str(drone.flyingState) + "\n")
		f.write("\n")
		f.write("\n")

	f.write("Estados \n")
	#drone.update(cmd=requestAllStatesCmd())
	print "Posicion  ",   drone.position
	print "Velocidad   ", drone.speed
	print "GPS    ",   drone.positionGPS
	print "Altitud   ", drone.altitude
	print "Estado    ",   drone.flyingState, "    Bateria   ", drone.battery
	
	f.write("Posicion  " + str(drone.position) + "\n")
	f.write("Velocidad   " + str(drone.speed) + "\n")
	f.write("GPS     " + str(drone.positionGPS) + "\n")
	f.write("Altitud     " + str(drone.altitude)  + "\n")
	f.write("Estado   " + str(drone.flyingState) + "\n")
	f.write("\n")
	f.write("\n")
	print ("Fin de vuelo")
	drone.land()



def prueba7(drone, velocidad, eje, tiempo):
	import commands as cm
	filename = "Datos_vuelo_prueba7" + eje + str(velocidad)+ ".txt"
	f = open(filename, "wb")
	f.write("Test de despegue y avance, velocidad 1   \n")
	drone.takeoff()
	print("")
	print("")
	print("")
	print("")
	print("Estado del drone")
	print("")
	i= 0
	for i in range(0,50):
		print "Posicion  ",   drone.position
		print "Velocidad   ", drone.speed
		print "GPS    ",   drone.positionGPS
		print "Altitud   ", drone.altitude
		print "Estado    ",   drone.flyingState, "    Bateria   ", drone.battery
		

	f.write("Movimiento      \n")
	f.write(eje +  str(velocidad)+ "\n")
	if eje == "cabeceo":
		drone.update( cmd=cm.movePCMDCmd( True, 0, velocidad, 0, 0 ) )

	elif eje == "balance":
		drone.update( cmd=cm.movePCMDCmd( True, velocidad, 0, 0, 0 ) )
	elif eje == "guinada":
		drone.update( cmd=cm.movePCMDCmd( True, 0, 0, velocidad, 0 ) )
	else:
		drone.land()
		f.write("Vuelo fallido")
	i= 0
	for i in range(0,tiempo):
		drone.update(cmd=cm.requestAllStatesCmd())
		print "Posicion  ",   drone.position
		print "Velocidad   ", drone.speed
		print "GPS    ",   drone.positionGPS
		print "Altitud   ", drone.altitude
		print "Estado    ",   drone.flyingState, "    Bateria   ", drone.battery
		f.write(str(i) + "\n")
		f.write("Posicion  " + str(drone.position) + "\n")
		f.write("Velocidad   " + str(drone.speed) + "\n")
		f.write("Actitud   " + str(drone.attitude) + "\n")
		f.write("GPS     " + str(drone.positionGPS) + "\n")
		f.write("Altitud     " + str(drone.altitude)  + "\n")
		f.write("Estado   " + str(drone.flyingState) + "\n")
		f.write("\n")
		f.write("\n")

	drone.update( cmd=cm.movePCMDCmd( True, 0, 0, 0, 0 ) )
	f.write("Parada de movimiento   \n")

	i= 0
	for i in range(0,20):
		print "Posicion  ",   drone.position
		print "Velocidad   ", drone.speed
		print "GPS    ",   drone.positionGPS
		print "Altitud   ", drone.altitude
		print "Estado    ",   drone.flyingState, "    Bateria   ", drone.battery
		f.write(str(i) + "\n")
		f.write("Posicion  " + str(drone.position) + "\n")
		f.write("Velocidad   " + str(drone.speed) + "\n")
		f.write("GPS     " + str(drone.positionGPS) + "\n")
		f.write("Altitud     " + str(drone.altitude)  + "\n")
		f.write("Estado   " + str(drone.flyingState) + "\n")
		f.write("\n")
		f.write("\n")

	print ("Fin de vuelo")
	drone.land()

def pruebaGPS(drone):
	
	f = open("Datos_vuelo_pruebaGPS.txt", "wb")
	f.write("Test de posicionGPS   \n")
	drone.takeoff()
	print("")
	print("")
	print("")
	print("")
	print("Estado del drone")
	print("")
	i= 0
	for i in range(0,500):
		print "Posicion  ",   drone.position
		print "Velocidad   ", drone.speed
		print "GPS    ",   drone.positionGPS
		print "Altitud   ", drone.altitude
		print "Estado    ",   drone.flyingState, "    Bateria   ", drone.battery
		f.write(str(drone.positionGPS)+ "\n")
		#f.write(str(i) + "\n")
		#f.write("Posicion  " + str(drone.position) + "\n")
		#f.write("Velocidad   " + str(drone.speed) + "\n")
		#f.write("GPS     " + str(drone.positionGPS) + "\n")
		#f.write("Altitud     " + str(drone.altitude)  + "\n")
		#f.write("Estado   " + str(drone.flyingState) + "\n")
		#f.write("\n")
		#f.write("\n")

	print ("Fin de vuelo")
	drone.land()


class dronefalso():
	def __init__(self):
		self.position=(0,0,0)
		self.speed= (0,0,0)
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

