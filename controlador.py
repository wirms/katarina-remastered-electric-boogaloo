import datetime
import commands
import os
import cuaternios as cua
import dibujar as dib
import numpy as np
import threading
import time


class Controlador():
	def __init__(self, drone):
		self.tiempo = 0.0
		self.posicion = [0,0,0]
		self.GPS = [0,0,0]
		self.drone = drone
		self.path = "./vuelos/" + datetime.datetime.now().strftime("Vuelo_%y%m%d_%H%M%S")
		if not os.path.exists(self.path):
			os.makedirs(self.path)

		self.nombrearchivos = (self.path + "/meta.txt", self.path + "/pos.txt",self.path + "/vel.txt",self.path + "/actitud.txt",self.path + "/GPS.txt")
		self.archivos = []
		for nombre in self.nombrearchivos:
			a = open(nombre, "wb")
			self.archivos.append(a)
		
		self.alineacion = False
		print ("Controlador creado e inicializado")
		print ("Logeando en     " + self.path)
		self.meta("Inicializacion")
		self.meta(self.path)
		self.velocidad= 20
		self.frecuencia = 0.1
		self.hilo = threading.Thread(target=self._escribirarchivos, args=())
		self.hilo.daemon = True
		self.hilo.start()
		self.feedback = True
		self.norte = 0.0
		
		
		self.hiloestimacion = threading.Thread(target=self._estimarposicion, args=())
		self.hiloestimacion.daemon = True
		self.hiloestimacion.start()

		self.hiloestado = threading.Thread(target=self._pedirestado, args=())
		self.hiloestado.daemon = True
		#self.hiloestado.start()
		self.hilorefrescar = threading.Thread(target=self._refrescar, args=())
		self.hilorefrescar.daemon = True
		#self.hilorefrescar.start()

		self.falso = False
		if isinstance(self.drone, Dronefalso):
			self.falso = True


	def navto(self, pos):
		pass


	def navto2(self,pos):
		try:
			if self.feedback:
				print ("Iniciando navegacion")
			self.meta("Navegando a    "+str(pos))
			roll, pitch, yaw, vert, dist = self._obtenerangulos(pos)
			roll, pitch, yaw, vert, dist = self.velocidad*roll, self.velocidad*pitch, self.velocidad*yaw, self.velocidad*vert, dist
			distmax = dist
			if not self.alineacion:
				yaw = 0
			
			while dist> 0.2:
				roll, pitch, yaw, vert, dist = self._obtenerangulos(pos)
				roll, pitch, yaw, vert, dist = self.velocidad*roll, self.velocidad*pitch, self.velocidad*yaw, self.velocidad*vert, dist
				if not self.alineacion:
					yaw = 0
				self.drone.update(cmd = commands.movePCMDCmd(True,roll,pitch,yaw,vert))
				if self.falso:
					self.drone.speed = [pitch, roll, vert]
				
				#if 100*dist/distmax % 10 == 0 and self.feedback:
				#	print (str(100 - 100*dist/distmax) + " %")

			if self.falso:
				self.drone.speed = [0, 0, 0]
			self.drone.update(cmd = commands.movePCMDCmd(True,0,0,0,0))
			
			if self.feedback:
				print ("Destino alcanzado")
			self.meta("Destino alcanzado   " + str(pos))
			return True

		except (KeyboardInterrupt, SystemExit):
			self.drone.update(cmd = commands.movePCMDCmd(True,0,0,0,0))
			if self.falso:
				self.drone.speed = [0, 0, 0]
			self.land()
			print ("Interrupcion manual, aterrizando")
			print
			self.meta("Interrupcion por teclado")
			return False

	def navGPS(self,pos):
		self.drone.update(cmd = commands.setHomeCmd(pos[0], pos[1], pos[2]))
		self.drone.update(cmd = commands.navigateHomeCmd())
	
	def _refrescar(self):
		while True:
			self.refrescar()
			time.sleep(0.1)

	def refrescar(self):
		print (self.drone.positionGPS)

	def test(self):

		self.drone.takeoff()
		time.sleep(1)
		self.drone.update( cmd=commands.movePCMDCmd(True, 20.0, 0.0, 0.0, 0.0) )
		try:
			time.sleep(2)
		except (KeyboardInterrupt, SystemExit):
			self.drone.update(cmd = commands.movePCMDCmd(True,0,0,0,0))
			self.drone.land()

		self.drone.land()

	def _navto(self):
		pos = self.posicionmantener
		roll = -self.drone.attitude[0]
		pitch = -self.drone.attitude[1]
		yaw = -self.drone.attitude[2]
		#roll, pitch, yaw, vert, dist = self._obtenerangulos(pos)
		#roll, pitch, yaw, vert, dist = self.velocidad*roll, self.velocidad*pitch, self.velocidad*yaw, self.velocidad*vert, dist
			
		if not self.alineacion:
			yaw = 0
			
		#if dist> 0.1:
		if True:
			roll = -self.drone.attitude[0]
			pitch = -self.drone.attitude[1]
			yaw = -self.drone.attitude[2]
			#roll, pitch, yaw, vert, dist = self._obtenerangulos(pos)
			#roll, pitch, yaw, vert, dist = self.velocidad*roll, self.velocidad*pitch, self.velocidad*yaw, self.velocidad*vert, dist
			
			if not self.alineacion:
				yaw = 0
			self.drone.update(cmd = commands.movePCMDCmd(True,roll,pitch,0,0))
				
		self.drone.update(cmd = commands.movePCMDCmd(True,0,0,0,0))
	def s(self):
		self.drone.update(cmd = commands.movePCMDCmd(True,0,0,0,0))

	def _estimarposicion(self):
		while True:
			self.estimarposicion()
			time.sleep(0.1)
	def estimarposicion(self):
		if self.drone.time == None:
			deltat = 0.0
		elif self.tiempo == None:
			deltat = self.drone.time
		else:
			deltat = self.drone.time - self.tiempo
		#print(deltat)	
		if deltat > 0:
			self.posicion = [self.posicion[0] + deltat*self.drone.speed[0],self.posicion[1] + deltat*self.drone.speed[1],self.posicion[2] + deltat*self.drone.speed[2]]
			#print(self.posicion)
			self.tiempo = self.drone.time

	def mantenerposicion(self,pos):
		#try:
		#	self.hilomantener.stop()
		#	self.meta("Posicion liberada")
		self.posicionmantener = pos
		self.meta("Manteniendo posicion")
		if self.feedback:
			print("Manteniendo posicion")
		self.hilomantener = threading.Thread(target=self._navto, args=())
		self.hilomantener.daemon = True
		self.hilomantener.start()

	def _obtenerangulos(self,pos):
		#Devuelve los comandos de control necesarios para volar a pos. Escalados [0,1] [roll, pitch, vert] unitario, yaw [0,1]

		kascenso = 1.0
		krotacion = 1.0
		a = [self.drone.position[0], self.drone.position[1], self.drone.altitude]
		b = pos

		act = self.drone.attitude
		act = [act[0],act[1],act[2]-self.norte]
		direccion = cua.director(b,a)
		dist = cua.norma(direccion)
		uz = [0,0,1]
		ux = [1,0,0]
		uy = [0,1,0]
		
		if dist<1e-6:
			return 0,0,0,0,0 

		direccion = cua.giro(direccion, uz, -act[2], rad = 1)
		
		for i in range(0,3):
			direccion[i] = direccion[i]/dist
		balance = direccion[1]
		vertical = kascenso*direccion[2]

		direccion0 = [direccion[0], direccion[1],0.0]
		
		cabeceo = direccion[0]
		balance = direccion[1]
		vertical = kascenso*direccion[2]

		guinada = cua.productoescalar(ux, direccion0)
		guinada = guinada / cua.norma(direccion0)
		guinada = np.arccos(guinada)
		if direccion[1]<0:
			guinada = -guinada
		guinada = krotacion*guinada / (2*np.pi)
		
		return balance, cabeceo, guinada, vertical, dist

	def _pedirestado(self):
		while True:
			self.pedirestado()
			time.sleep(0.1)

	def pedirestado(self):
		self.drone.update(cmd = commands.requestAllStatesCmd())

	def _escribirarchivos(self):
		while True:

			self.escribirarchivos()
			time.sleep(self.frecuencia)



	def escribirarchivos(self):
		if not (self.drone.time == self.tiempo):
			#Posicion, posicion 1
			if self.drone.time == None:
				self.archivos[1].write("{:<16f}".format(0.0))
			else:
				self.archivos[1].write("{:<16f}".format(self.drone.time))
			self.archivos[1].write("   ")
			self.archivos[1].write("{:<16f}".format(self.drone.position[0]))
			self.archivos[1].write("   ")
			self.archivos[1].write("{:<16f}".format(self.drone.position[1]))
			self.archivos[1].write("   ")
			self.archivos[1].write("{:<16f}".format(self.drone.altitude))
			self.archivos[1].write("   ")
			self.archivos[1].write("{:<16f}".format(self.drone.position[2]))
			self.archivos[1].write("   ")
			self.archivos[1].write("{:<16f}".format(self.posicion[0]))
			self.archivos[1].write("   ")
			self.archivos[1].write("{:<16f}".format(self.posicion[1]))
			self.archivos[1].write("   ")
			self.archivos[1].write("{:<16f}".format(self.posicion[2]))
			self.archivos[1].write("   ")
			self.archivos[1].write("\n")
			
			#Velocidad, posicion 2
			if self.drone.time == None:
				self.archivos[2].write("{:<16f}".format(0.0))
			else:
				self.archivos[2].write("{:<16f}".format(self.drone.time))
			self.archivos[2].write("   ")
			self.archivos[2].write("{:<16f}".format(self.drone.speed[0]))
			self.archivos[2].write("   ")
			self.archivos[2].write("{:<16f}".format(self.drone.speed[1]))
			self.archivos[2].write("   ")
			self.archivos[2].write("{:<16f}".format(self.drone.speed[2]))
			self.archivos[2].write("   ")
			self.archivos[2].write("\n")

			#Actitud, posicion 3
			if self.drone.time == None:
				self.archivos[3].write("{:<16f}".format(0.0))
			else:	
				self.archivos[3].write("{:<16f}".format(self.drone.time))
			self.archivos[3].write("   ")
			self.archivos[3].write("{:<16f}".format(self.drone.attitude[0]))
			self.archivos[3].write("   ")
			self.archivos[3].write("{:<16f}".format(self.drone.attitude[1]))
			self.archivos[3].write("   ")
			self.archivos[3].write("{:<16f}".format(self.drone.attitude[2]))
			self.archivos[3].write("   ")
			self.archivos[3].write("\n")

			#PosicionGPS, posicion 4
			if self.drone.time == None:
				self.archivos[4].write("{:<16f}".format(0.0))
			else:
				self.archivos[4].write("{:<16f}".format(self.drone.time))
			self.archivos[4].write("   ")
			self.archivos[4].write("{:<16f}".format(self.drone.positionGPS[0]))
			self.archivos[4].write("   ")
			self.archivos[4].write("{:<16f}".format(self.drone.positionGPS[1]))
			self.archivos[4].write("   ")
			self.archivos[4].write("{:<16f}".format(self.drone.positionGPS[2]))
			self.archivos[4].write("   ")
			self.archivos[4].write("{:<16f}".format(self.drone.altitude))
			self.archivos[4].write("   ")
			self.archivos[4].write("\n")


			self.tiempo = self.drone.time
	def meta(self, mensaje):
		self.archivos[0].write(str(self.drone.time))
		self.archivos[0].write("    ")
		self.archivos[0].write(mensaje)
		self.archivos[0].write("\n")

	def land(self):
		try:
			self.drone.land()
			self.meta("Aterrizando")
			if self.feedback:
				print ("Aterrizando")
		except:
			self.drone.emergency()
			self.meta("Emergencia")
			if self.feedback:
				print ("Emergencia")
	def takeoff(self):
		self.meta("Despegando")
		if self.feedback:
			print ("Despegando")
		self.drone.takeoff()

	def dibujar(self):
		ruta = self.nombrearchivos[1]
		dib.dibujartrayectoria(ruta)

class Dronefalso():
	def __init__(self):
		self.position=[0,0,0]
		self.speed= [0,0,0]
		self.attitude = [0,0,0]
		self.positionGPS=[0,0,0]
		self.altitude = 0.0
		self.flyingState=0
		self.battery = 0
		self.time = 0
		
		self.testmovimiento()

	def takeoff(self):
		return
	def land(self):
		return
	def update(self, cmd = None):
		return
	def flyToAltitude(self, h):
		return
	def requestAllStates(self):
		return
	def testmovimiento(self):
		self.hilo = threading.Thread(target=self._testmovimiento, args=())
		self.hilo.daemon = True
		self.hilo.start()
	def _testmovimiento(self):
		while True:
			self.time = self.time + 0.1
			self.position[0] = self.position[0] + self.speed[0]/10.0
			self.position[1] = self.position[1] + self.speed[1]/10.0
			self.position[2] = self.position[2] + self.speed[2]/10.0
			self.altitude = self.altitude + self.speed[2]/10.0
			time.sleep(0.1)


class GUIdrone():
	def __init__(self,drone):
		import Tkinter as tk 
		import ttk
		self.drone = drone
		root = tk.Tk()

		framebase = ttk.Frame(root)
		areapos = ttk.Frame(framebase)
		areaGPS = ttk.Frame(framebase)
		areaterminal = ttk.Frame(framebase, height = 400, width = 500)
		pos = ttk.Label(areapos, text = "Posicion")
		self.pos2 = ttk.Label(areapos, text = " 0   0   0")
		GPS = ttk.Label(areapos, text = "GPS")
		self.GPS2 = ttk.Label(areapos, text = "0   0   0")
		framebase.pack()
		areapos.pack(side = tk.RIGHT)
		areaGPS.pack(side = tk.RIGHT)
		pos.grid(row = 1, column = 1)
		self.pos2.grid(row = 2, column = 1)
		GPS.grid(row = 1, column = 2)
		self.GPS2.grid(row = 2, column = 2)
		areaterminal.pack(side = tk.LEFT)
		wid = areaterminal.winfo_id()
		os.system("xterm -into %d -geometry 40x20 -sb &" %wid)
		root.mainloop()
		self.hilorefresco = threading.Thread(target=self._refrescar, args=())
		self.hilorefresco.daemon = True
		self.hilorefresco.start()
		

	def refrescar(self):
		textopos = str(self.drone.position[0])+ "   " + str(self.drone.position[1])+ "   " + str(self.drone.position[2])
		self.pos2.config(text=textopos)
		textoGPS = str(self.drone.positionGPS[0])+ "   " + str(self.drone.positionGPS[1])+ "   " + str(self.drone.positionGPS[2])
		self.GPS2.config(text=textoGPS)
		self.pos2.update_idletasks()
		self.GPS2.update_idletasks()
        
	def _refrescar(self):
		self.refrescar()
    	time.sleep(0.1)
#PRUEBAS
